import telebot
from telebot import types
from datetime import datetime

# API_TOKEN = '7245674895:AAFrEJukU4c46Ie7mq7zZoVttmhCUmDg57o'
bot = telebot.TeleBot("7903847896:AAH3vRhLsrhcBdruoH_f-_kh5vaxU57ZMpQ")

import json


def get_schedule(day):
    with open('schedule.json', 'r', encoding='utf-8') as file:
        schedule = jso4n.load(file)

    week_number = datetime.now().isocalendar()[1]
    week_type = 'Znam' if week_number % 2 == 0 else 'Chisl'

    return schedule[week_type].get(day, [])


# def get_schedule():
#     with open('schedule.json', 'r', encoding='utf-8') as file:
#         schedule = json.load(file)
#
#     today = datetime.now().strftime('%A')
#     week_number = datetime.now().isocalendar()[1]
#     week_type = 'Znam' if week_number % 2 == 0 else 'Chisl'
#
#     return schedule[week_type].get(today, [])


def create_weekday_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    buttons = [
        types.KeyboardButton('Monday'),
        types.KeyboardButton('Tuesday'),
        types.KeyboardButton('Wednesday'),
        types.KeyboardButton('Thursday'),
        types.KeyboardButton('Friday'),
        types.KeyboardButton('Saturday'),
        types.KeyboardButton('Sunday')
    ]
    markup.add(*buttons)
    return markup


#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я бот, который сообщает расписание занятий на сегодня. Используйте команду /schedule для получения расписания.")
#
# @bot.message_handler(commands=['schedule'])
# def send_schedule(message):
#     schedule = get_schedule()
#     if schedule:
#         schedule_text = '\n'.join(schedule)
#         bot.reply_to(message, f'Расписание на сегодня:\n{schedule_text}')
#     else:
#         bot.reply_to(message, 'Сегодня занятий нет.')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который сообщает расписание занятий. Выберите день недели:",
                 reply_markup=create_weekday_buttons())


@bot.message_handler(
    func=lambda message: message.text in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
def send_schedule(message):
    day = message.text
    schedule = get_schedule(day)
    if schedule:
        schedule_text = '\n'.join(schedule)
        bot.reply_to(message, f'Расписание на {day}:\n{schedule_text}')
    else:
        bot.reply_to(message, f'На {day} занятий нет.')


bot.polling(none_stop=True)