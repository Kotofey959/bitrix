from aiogram import Bot

BOT_TOKEN = "5937470704:AAEmI-qYRIRAihYAhWY6rT6i8BUPu1lwiNk"
CHAT_ID = -1002146063171

bot = Bot(BOT_TOKEN)


def get_message_text(parsed_info: dict):
    """
    Формируем сообщение для отправки в telegram
    :param parsed_info:
    :return:
    """
    return f"ID:  {parsed_info.get('id')}\n" \
           f"Имя контакта:  {parsed_info.get('name') or 'Нет'}\n" \
           f"Комментарий:  {parsed_info.get('comments') or 'Нет'}\n" \
           f"Телефон:  {parsed_info.get('phone') or 'Нет'}\n" \
           f"Оценка площадки:  {parsed_info.get('place_score') or 'Нет'}\n" \
           f"Вы бы посоветовали Scandy Park:  {parsed_info.get('recommendation') or 'Нет'}\n" \
           f"Вы проводили праздник в нашем парке:  {parsed_info.get('holiday') or 'Нет'}\n" \
           f"Оцените качество обслуживающего персонала:  {parsed_info.get('personal_score') or 'Нет'}\n" \
           f"Оцените качество аттракционов по пятибалльной шкале:  {parsed_info.get('attraction_score') or 'Нет'}\n"


async def send_message(parsed_info: dict):
    """
    Отправка сообщения в канал

    :param parsed_info:
    :return:
    """
    message_text = get_message_text(parsed_info)
    await bot.send_message(CHAT_ID, message_text)
