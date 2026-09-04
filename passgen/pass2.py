import secrets
import string


def get_password_length():
    """Запитує у користувача довжину пароля та перевіряє введення."""
    while True:
        try:
            length = int(
                input("Введіть бажану довжину пароля (мінімум 8 символів): ")
            )
            if length < 8:
                print("⚠️ Пароль занадто короткий для надійного захисту. Спробуйте ще раз.")
                continue
            return length
        except ValueError:
            print("❌ Будь ласка, введіть коректне ціле число.")


def generate_secure_password(length):
    """Генерує криптографічно стійкий пароль із гарантованим вмістом усіх типів символів."""
    # Визначаємо набори символів
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    # 1. Гарантуємо наявність мінімум одного символу з кожної групи
    guaranteed_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    # 2. Визначаємо, скільки ще символів потрібно згенерувати
    remaining_length = length - len(guaranteed_chars)

    # Об'єднуємо всі символи для заповнення решти пароля
    all_characters = lower + upper + digits + symbols

    # 3. Генеруємо решту символів
    remaining_chars = [
        secrets.choice(all_characters) for _ in range(remaining_length)
    ]

    # 4. Об'єднуємо обидва списки символів
    password_list = guaranteed_chars + remaining_chars

    # 5. Криптографічно безпечно перемішуємо список символів,
    # щоб гарантовані символи не завжди стояли на початку пароля.
    secrets.SystemRandom().shuffle(password_list)

    # Збираємо список у фінальний рядок
    return "".join(password_list)


# Головний запуск програми
if __name__ == "__main__":
    print("--- Надійний генератор паролів ---")
    user_length = get_password_length()
    secure_password = generate_secure_password(user_length)

    print("\n✅ Ваш новий безпечний пароль:")
    print(secure_password)
