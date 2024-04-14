"""Описание маршрутов и их внутренней логики в представлении FastAPI."""
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
    """Хелсчек-метод, показывает hostname текущего инстанса."""
    return HealthResponse()


@app.post("/new")
def new(request_body: dict):
    """Получает секретноее сообщение, сохраняет в базе, отдает uuid записи."""
    request_body = NewRequest.init_from_dict(request_body)
    response_body = NewResponse()

    try:
        message_text_to_insert = request_body.message_text
        saved_message_uuid = db.insert(message_text_to_insert)
    except Exception as e:
        response_body.error = e
    else:
        response_body.message_id = saved_message_uuid
    finally:
        return response_body


@app.post("/read")
def read(request_body: dict):
    """Получает uuid секретного сообщения, находит его в базе, удаляет, возвращает текст сообщения."""
    request_body = ReadRequest.init_from_dict(request_body)
    response_body = ReadResponse()

    try:
        uuid_to_read = request_body.message_id
        extracted_text = db.select(uuid_to_read)
        db.delete(uuid_to_read)
    except Exception as e:
        response_body.error = e
    else:
        response_body.message_text = extracted_text
    finally:
        return response_body


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)