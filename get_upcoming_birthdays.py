from datetime import datetime

def get_upcoming_birthdays(users) -> list:
    current_date = datetime.today().date()
    congratulations = []
    congratulation_date = current_date
    for user in users:
        birthday_this_year = datetime.strptime(user['birthday'], '%Y.%m.%d').replace(year=2024).date()
        if birthday_this_year < current_date:
            congratulation_date = birthday_this_year.replace(year=current_date.year + 1)
        else:
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year.replace(day=birthday_this_year.day + 2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year.replace(day=birthday_this_year.day + 1)
            # Розглянути дату на наступний рік???
        user['birthday'] = datetime.strftime(congratulation_date, '%Y.%m.%d')
        congratulations.append(user)
    print(congratulations)

users = [
    {"name": "John Doe", "birthday": "1985.01.30"},
    {"name": "Jane Smith", "birthday": "1990.02.24"}
]

get_upcoming_birthdays(users)