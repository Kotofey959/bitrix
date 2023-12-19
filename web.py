from flask import Flask, request

import uvicorn
from pydantic import BaseModel

app = Flask(__name__)

BITRIX_TOKEN = "ueqd3rweu1k5z52xnyk5zcr17m3zoxqy"


@app.route("/lead", methods=["POST"])
async def get_new_lead():
    """
    Обработка нового лида

    :return:
    """
    print("Зашли сюда")
    data = request.get_json()
    print(data)

if __name__ == "__main__":
    try:
        print("Сервер запущен")
        uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
    except:
        print("Ошибка")
