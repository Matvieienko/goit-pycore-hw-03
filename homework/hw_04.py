from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Повертає список користувачів з інформацією про дні народження на наступний тиждень,
    враховуючи вихідні і переносить привітання на понеділок, якщо потрібно.
    
    :param users: list - список користувачів, де кожен користувач має ключі "name" та "birthday".
    :return: list - список словників з іменами користувачів та датами привітання.
    """
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо день народження користувача у datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Отримуємо день народження цього року
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув цього року, беремо дату наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Якщо день народження відбувається на наступному тижні
        if today <= birthday_this_year <= next_week:
            # Якщо день народження випадає на вихідний (субота або неділя), переносимо на понеділок
            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя
                birthday_this_year += timedelta(days=1)
            
            # Додаємо користувача до списку привітань
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.10.08"},
    {"name": "Jane Smith", "birthday": "1990.10.09"},
    {"name": "John Smith", "birthday": "1995.10.10"},
    {"name": "Jane Doe", "birthday": "1989.10.11"},
    {"name": "Michael Jackson", "birthday": "1958.08.29"},
    {"name": "Kim Noel Kardashian", "birthday": "1980.10.21"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
