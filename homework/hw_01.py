from datetime import datetime 

""" 
# Моя перша версія
def get_days_from_today(date):
    try:
        current_date = datetime.today().date()
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        difference = input_date - current_date
        return print(f'Різниця в днях між {current_date} та {input_date}:', difference.days)
    except:
        return print('Невірний формат дати. Використовуйте формат YYYY-MM-DD.')

date = input('Input date YYYY-MM-DD: ')
get_days_from_today(date) """


"""
# Моя друга версія
def get_days_from_today(date):
    try:
        difference = datetime.strptime(date, '%Y-%m-%d').date() - datetime.today().date() # Різниця між введеною датою і поточною датою
        return print(f'Різниця в днях між поточною датою та {date}:', difference.days) # Виводимо результат
    except:
        return print('Невірний формат дати. Використовуйте формат YYYY-MM-DD.') # Обробляємо помилку формату дати

date = input('Введить дату YYYY-MM-DD: ') # Отримуємо дату від користувача
get_days_from_today(date) # Викликаємо функцію """


# То як поправив код ChatGPT
def get_days_from_today(date):
    try:
        # Різниця між введеною датою і поточною датою
        difference = datetime.strptime(date, '%Y-%m-%d').date() - datetime.today().date()
        return difference.days  # Повертаємо кількість днів
    except ValueError:  # Обробляємо помилку формату дати
        return 'Невірний формат дати. Використовуйте формат YYYY-MM-DD.'

# Отримуємо дату від користувача
date = input('Введіть дату YYYY-MM-DD: ')

# Викликаємо функцію та виводимо результат
days_difference = get_days_from_today(date)
print(f'Різниця в днях між поточною датою та {date}:', days_difference)
