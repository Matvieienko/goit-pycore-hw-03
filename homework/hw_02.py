import random


def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує набір унікальних випадкових чисел у заданому діапазоні та повертає відсортований список.
    
    :param min_num: int - мінімальне можливе число у наборі не менше 1.
    :param max_num: int - максимальне можливе число у наборі не більше 1000.
    :param quantity: int - кількість чисел, які потрібно вибрати значення між min і max.
    :return: list - відсортований список випадкових чисел або порожній список, якщо параметри невірні.
    """
    # Перевірка коректності вхідних даних
    if not (1 <= min_num <= 1000 and 1 <= max_num <= 1000 and min_num < max_num):
        return ["Невірний діапазон, має бути від 1 до 1000"]  # Повертаємо список з параметрами діапазону, якщо дані некоректні
    if quantity > (max_num - min_num + 1) or quantity <= 0:
        return ["Невірна кількість"]  # Якщо кількість чисел більша за можливий діапазон або менша за 1
    
    # Генеруємо випадкові унікальні числа
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(numbers)

# Приклад використання 
your_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші числа:", your_numbers)
