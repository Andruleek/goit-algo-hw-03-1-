from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримуємо поточну дату
        today = datetime.now().date()
        # Розраховуємо різницю у днях
        delta = input_date - today
        # Повертаємо кількість днів (як ціле число)
        return delta.days
    except ValueError:
        # Обробка помилки у випадку неправильного формату дати
        raise ValueError("Дата має бути у форматі 'РРРР-ММ-ДД'")

# Приклад використання
print(get_days_from_today('2024-11-25'))  # Змінюйте дату для перевірки

