import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до стандартного міжнародного формату.
    Видаляє зайві символи і додає код +38 для українських номерів без міжнародного префікса.
    
    :param phone_number: str - Номер телефону у різному форматі.
    :return: str - Нормалізований номер телефону у форматі +380XXXXXXXXX.
    """
    # Видаляємо всі символи, крім цифр і плюса
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    # Видаляємо зайві плюси, залишаємо тільки один на початку
    cleaned_number = re.sub(r'^\++', '+', cleaned_number)
    
    # Якщо номер починається з '380', додаємо тільки '+'
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    
    # Якщо номер починається з '0', додаємо '+38'
    if cleaned_number.startswith('0'):
        return '+38' + cleaned_number.lstrip('0')
    
    # Якщо номер вже має '+', просто повертаємо його
    if cleaned_number.startswith('+'):
        return cleaned_number
    
    # Якщо немає міжнародного коду, додаємо '+38'
    return '+38' + cleaned_number

# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+++++++38(095)1518081"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)