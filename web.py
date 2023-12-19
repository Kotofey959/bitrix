import uvicorn
from urllib.parse import parse_qs
from fastapi import FastAPI, Request
import requests

from bot import send_message

app = FastAPI()
BITRIX_TOKEN = "ueqd3rweu1k5z52xnyk5zcr17m3zoxqy"

PLACE_SCORE = {
    "1883": 1,
    "1885": 2,
    "1887": 3,
    "1889": 4,
    "1891": 5
}

RECOMMENDATION = {
    "1903": "Определенно Да",
    "1905": "Скорее всего да",
    "1907": "Скорее всего нет",
    "1909": "Определенно нет"
}

HOLIDAY = {
    "1919": "В восторге! Праздник провели на высшем уровне",
    "1921": "Все понравилось, но были недочеты",
    "1923": "Не понравилось",
    "1925": "Не проводили еще праздники в Scandy Park"
}

PERSONAL_SCORE = {
    "1927": 1,
    "1929": 2,
    "1931": 3,
    "1933": 4,
    "1935": 5
}

ATTRACTION_SCORE = {
    "1945": 1,
    "1947": 2,
    "1949": 3,
    "1951": 4,
    "1953": 5
}

used_ids = set({})


@app.post("/lead")
async def get_new_lead(request: Request):
    """
    Обработка нового лида
    :return:
    """
    print("Зашли сюда")
    try:
        response = await request.body()
        decoded_response = response.decode("utf-8")

        data = parse_qs(decoded_response)

        lid_ids: list[str] = data.get("data[FIELDS][ID]")

        if not lid_ids:
            return

        lid_id = lid_ids[0]
        if lid_id in used_ids:
            return
        lead_info = get_lid_info(lid_id)
        result = lead_info.get("result")
        if not result or result.get("STATUS_ID") != "20":
            return
        parsed_info = parse_lid_info(lead_info)
        await send_message(parsed_info)
        used_ids.add(lid_id)
        if len(used_ids) > 99:
            used_ids.clear()

    except:
        print("Не смогли достать json")


def get_lid_info(lid_id: str):
    """

    :param lid_id:
    :return:
    """
    link = f"https://lasvegas.bitrix24.ru/rest/47181/3eggrep7any8rvue/crm.lead.get?id={lid_id}"
    try:
        return requests.get(link).json()
    except:
        print("Не пошло")


def parse_lid_info(lid_info: dict):
    result = lid_info.get("result")

    return {
        "place_score": PLACE_SCORE.get(result.get("UF_CRM_1694005680")),
        "recommendation": RECOMMENDATION.get(result.get("UF_CRM_1694005757")),
        "holiday": HOLIDAY.get(result.get("UF_CRM_1694005820")),
        "personal_score": PERSONAL_SCORE.get(result.get("UF_CRM_1694005866")),
        "attraction_score": ATTRACTION_SCORE.get(result.get("UF_CRM_1694005908")),
        "id": result.get("ID"),
        "name": result.get("NAME"),
        "comments": result.get("comments"),
        "phone": result.get("phone")
    }


if __name__ == "__main__":
    try:
        print("Сервер запущен")
        uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
    except:
        print("Ошибка")
