import datetime

# Получить текущую дату
current_date = datetime.date.today()

# Получить номер недели
week_number = current_date.isocalendar()[1]

# Получить день недели (0 - понедельник, 6 - воскресенье)
day_of_week = current_date.weekday()

# Список названий дней недели
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

# Вывод номера недели и дня недели
print(f"Номер недели: {week_number}")
print(f"День недели: {days[day_of_week]}")