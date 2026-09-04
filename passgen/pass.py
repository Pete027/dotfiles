import secrets
import string

# Використовуємо вбудовані надійні набори символів
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
# Стандартні безпечні спецсимволи (без специфічних знаків типу №)
symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

# Об'єднуємо всі символи в один алфавіт
all_characters = lower + upper + digits + symbols

# Задаємо довжину пароля
length = 16

# Генеруємо криптографічно стійкий пароль із повтореннями символів
password = "".join(secrets.choice(all_characters) for _ in range(length))

print(password)
