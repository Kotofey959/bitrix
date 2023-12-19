from typing import Any
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
app = FastAPI()
BITRIX_TOKEN = "ueqd3rweu1k5z52xnyk5zcr17m3zoxqy"


@app.post("/lead")
async def get_new_lead(request: Request):
    """
    Обработка нового лида
    :return:
    """
    print("Зашли сюда")
    try:
        data = await request.body()
        print(data)
    except:
        print("Не смогли достать json")

if __name__ == "__main__":
    try:
        print("Сервер запущен")
        uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
    except:
        print("Ошибка")
