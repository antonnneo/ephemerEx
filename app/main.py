from fastapi import FastAPI
import uvicorn
from modules import execute

app = FastAPI()

@app.get("/health/")
def health():
    return 'healthy'


@app.post("/new/")
def new_note(note_data):
    text = note_data.get("text")
    print(text)
    result = execute(f"""
    INSERT INTO messages
            ("content")
    VALUES
            ('{text}')
    RETURNING
        id;
    """)
    
    return {"id": f"{result}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)