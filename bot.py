from aiogram import Bot

BOT_TOKEN = "5937470704:AAEmI-qYRIRAihYAhWY6rT6i8BUPu1lwiNk"
CHAT_ID = -1002146063171

bot = Bot(BOT_TOKEN)


def get_message_text(parsed_info: dict):
    return f"ID: {parsed_info.get('id')}\n" \
           f"Имя контакта: {parsed_info.get('name')}\n" \
           f"Комментарий: {parsed_info.get('comments')}\n" \
           f"Телефон: {parsed_info.get('phone')}\n" \
           f"Оценка площадки: {parsed_info.get('place_score')}"


async def send_message(parsed_info: dict):
    """
    Отправка сообщения в канал

    :param parsed_info:
    :return:
    """
    message_text = get_message_text(parsed_info)
    await bot.send_message(CHAT_ID, message_text)
