import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка коректності введених параметрів
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    # Повернення відсортованого списку
    return sorted(numbers)

# Приклад використання:
print(get_numbers_ticket(1, 49, 6))  
print(get_numbers_ticket(5, 15, 7))  
