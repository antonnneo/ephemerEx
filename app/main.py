import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from interfaces.api_contracts.health.response import HealthResponse
from interfaces.api_contracts.new.request import NewRequest
from interfaces.api_contracts.new.response import NewResponse
from interfaces.api_contracts.read.request import ReadRequest
from interfaces.api_contracts.read.response import ReadResponse
from interfaces.database import DataBase


db = DataBase()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    """ healthcheck """
    return HealthResponse()


@app.post("/new")
def new(data: dict):
    """ receive text, save it to db and return uuid of entry """
    data = NewRequest.init_from_dict(data)

    return NewResponse(message_id=db.insert(data.message_text))


@app.post("/read")
def read(data: dict):
    """ get message's UUID, delete it from db and return text """
    data = ReadRequest.init_from_dict(data)

    message_text = db.select(data.message_id)
    db.delete(data.message_id)

    return ReadResponse(message_text=message_text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)