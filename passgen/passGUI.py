import secrets
import string
import tkinter as tk
from tkinter import messagebox


def generate_secure_password(length):
    """Генерує надійний пароль із гарантованим вмістом усіх типів символів."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    # Гарантуємо наявність мінімум одного символу з кожної групи
    guaranteed_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    remaining_length = length - len(guaranteed_chars)
    all_characters = lower + upper + digits + symbols

    remaining_chars = [
        secrets.choice(all_characters) for _ in range(remaining_length)
    ]
    password_list = guaranteed_chars + remaining_chars

    # Перемішуємо безпечно
    secrets.SystemRandom().shuffle(password_list)
    return "".join(password_list)


def on_generate():
    """Обробник натискання кнопки генерації."""
    length = length_slider.get()
    password = generate_secure_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def on_copy():
    """Копіює пароль у буфер обміну."""
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Зберігає дані в буфері після закриття
        messagebox.showinfo("Успіх", "Пароль скопійовано в буфер обміну! ✅")
    else:
        messagebox.showwarning("Помилка", "Спершу згенеруйте пароль! ⚠️")


# Налаштування головного вікна
root = tk.Tk()
root.title("Secure PassGen")
root.geometry("400x250")
root.resizable(False, False)

# Елементи інтерфейсу
title_label = tk.Label(
    root, text="Генератор надійних паролів", font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

# Повзунок довжини
slider_frame = tk.Frame(root)
slider_frame.pack(pady=5)
slider_label = tk.Label(slider_frame, text="Довжина пароля:")
slider_label.pack(side=tk.LEFT, padx=5)
length_slider = tk.Scale(slider_frame, from_=8, to=32, orient=tk.HORIZONTAL)
length_slider.set(16)  # Стандартна довжина
length_slider.pack(side=tk.LEFT)

# Поле для виведення пароля
password_entry = tk.Entry(
    root, font=("Courier New", 12), width=30, justify="center"
)
password_entry.pack(pady=10)

# Кнопки дії
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

generate_btn = tk.Button(
    button_frame, text="Згенерувати", command=on_generate, bg="#4CAF50", fg="white"
)
generate_btn.pack(side=tk.LEFT, padx=10)

copy_btn = tk.Button(button_frame, text="Скопіювати", command=on_copy)
copy_btn.pack(side=tk.LEFT, padx=10)

# Запуск вікна
root.mainloop()
