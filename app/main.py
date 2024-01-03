from fastapi import FastAPI
import uvicorn
import os
from modules import execute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    """ just healthcheck """
    return {
        "instanceId": os.environ.get("HOSTNAME"),
        "status": "healthy"
    }


@app.post("/new")
def new_note(contract: dict):
    """ receive the text of the message and save it to the database
    assign uuid and return it in the response """

    text = contract.get("text")
    if text is not None:
        result = execute(f"""
            INSERT INTO messages ("content")
            VALUES ('{text}')
            RETURNING id;""")
        return {
            "instanceId": os.environ.get("HOSTNAME"),
            "id": f"{result}"
        }
    else:
        return {
            "instanceId": os.environ.get("HOSTNAME"),
            "error": "there is no field 'text' in request"
        }
    
    

@app.post("/read")
def new_note(contract: dict):
    """ get the UUID of the message
    delete the message with represented UUID and return message's text at response """

    id = contract.get("id")
    result = execute(f"""
        SELECT "content" 
        FROM messages
        where id = '{id}';""")

    execute(f"""
        DELETE FROM messages
        WHERE id = '{id}';""")

    if result is None:
        return {
            "instanceId": os.environ.get("HOSTNAME"),
            "error": f"message with id '{id}' not found"
        }
    else:
        return {
            "instanceId": os.environ.get("HOSTNAME"),
            "message": f"{result}"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)