import telebot  # библиотека TelegramBotAPI
from telebot import types  # для создания кнопок и тд.

bot = telebot.TeleBot("6304999378:AAHD8Hr_XILMsZa2naTZTxb5l8xtIZgTZRM")


@bot.message_handler(commands=["start"])  # обработка команды start
def main(message):
    bot.send_message(message.chat.id, "hello")  # вывод сообрщения


@bot.message_handler(content_types=["photo"])  # обработка фото в скобках можно задать любой тип
def get_photo(message):
    markup = types.InlineKeyboardMarkup()  # создание кнопки
    # markup.add(types.InlineKeyboardButton("изменить фото?", callback_data="edit"))
    # markup.add(types.InlineKeyboardButton("delete this photo?", callback_data="delete"))
    # markup.add(types.InlineKeyboardButton("go to sayt", url="https://stepik.org"))  # кнопка со ссылкой
    # bot.reply_to(message, "there is beautiful", reply_markup=markup)  # вывод сообщения и кнопки

    # МОЖНО ИГРАТЬ С РАСПОЛОЖЕНИЕМ КНОПОК
    but1 = (types.InlineKeyboardButton("go to sayt", url="https://stepik.org"))
    markup.row(but1)  # ставит кнопку but1 на 1 позицию

    but2 = (types.InlineKeyboardButton("delete this photo?", callback_data="delete"))
    but3 = (types.InlineKeyboardButton("изменить фото?", callback_data="edit"))
    markup.row(but2, but3)  # ставит кнопки but2 и but3 на 2 позицию

    bot.reply_to(message, "This is beautiful)", reply_markup=markup)


# на данный момент наши кнопки не выполняют никаких ф-ий, поэтому напишем для них ф-ию
@bot.callback_query_handler(func=lambda callback: True)  # callback_query обрабатывает callback_date в стороках 15, 16)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text("edit text", callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)  # с помощью нее бот работыкт на постоянку
