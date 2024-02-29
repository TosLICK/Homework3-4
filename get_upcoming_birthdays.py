from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users: list) -> list:
    current_date = datetime.today().date() # визначаємо поточну дату
    congratulations = []
    for user in users:
        congratulation_date = current_date
        birthday_this_year = datetime.strptime(user['birthday'], '%Y.%m.%d').replace(year=2024).date() # визначаємо день народження цього року
        if current_date <= birthday_this_year <= current_date + timedelta(days=6): # Беремо дати в найближчі 7 днів з сьогоднішнього
            if birthday_this_year.weekday() == 5: # якщо день народження (д.н.) припадає на суботу, вітання переносимо на ПН
                congratulation_date = birthday_this_year.replace(day=birthday_this_year.day + 2)
            elif birthday_this_year.weekday() == 6: # якщо д.н. припадає на неділю, вітання переносимо на ПН
                congratulation_date = birthday_this_year.replace(day=birthday_this_year.day + 1)
            else:
                congratulation_date = birthday_this_year # якщо д.н. припадає на інший день тижня, вітаємо в д.н.
            user['congratulation_date'] = datetime.strftime(congratulation_date, '%Y.%m.%d') # переводимо дату вітання в рядок і додаємо до словника
            del user['birthday'] # видаляємо зі словника дату дня народження, залишаємо дату вітання
            congratulations.append(user)
    return congratulations

# users = [
#     {"name": "John Doe", "birthday": "1985.01.30"},
#     {"name": "Tolik", "birthday": "2004.02.29"},
#     {"name": "Anna", "birthday": "1979.02.28"},
#     {"name": "Olha", "birthday": "1993.03.06"},
#     {"name": "Andrii", "birthday": "1993.03.02"},
#     {"name": "Oleh", "birthday": "1993.03.03"},
#     {"name": "Jane Smith", "birthday": "1992.03.07"}
# ]

# upcoming_birthdays = get_upcoming_birthdays(users)
# print(upcoming_birthdays)