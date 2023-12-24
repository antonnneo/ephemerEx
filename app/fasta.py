from fastapi import FastAPI
import uvicorn
from modules import execute, generate_text
from datetime import datetime
from uuid import uuid4

app = FastAPI()

@app.get("/health/")
def health():
    return 'healthy'


@app.post("/new/")
def new_note():
    result = execute(f"""
    INSERT INTO messages
            ("content")
    VALUES
            ('{generate_text(10_000)}')
    RETURNING
        id;
    """)

    return {"id": f"{result}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)