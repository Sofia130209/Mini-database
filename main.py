from tkinter import *
from tkinter import ttk
import json

window = Tk()
window.title("Add a new person")
window.iconbitmap("images/main_icon.ico")
window.geometry("700x750")
window.config(bg='lightblue')
window.resizable(False, False) # окно невозможно изменят по размеру

# -----Функции-----
def write_to_json():
    res = {field: entries[field].get() for field in fields}

    try:
        with open('_user.json', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

    data.append(res)

    with open('_user.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    written.place(relx=0.5, rely=1.0, anchor='s', y=-190)

def clear():
    for entry in entries.values():
        entry.delete(0, END)

    written.place_forget()

# -----Функция для просмотра базы данных в отдельном окне-----
def view_database():
    database = Tk()
    database.iconbitmap("images/icon.ico")
    database.title("Database")
    database.geometry("700x750")
    database.config(bg='lightblue')
    database.resizable(False, False) # окно невозможно изменят по размеру

    # Заголовок окна
    title = Label(database, text="Database View", font=("JetBrains mono", 20), bg='lightblue')
    title.pack(pady=20)

    # Создание фрейма для таблицы
    frame = Frame(database, bg='lightblue')
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Использование ttk.Treeview для отображения таблицы
    tree = ttk.Treeview(frame, columns=fields, show='headings', height=20)
    tree.pack(fill=BOTH, expand=True)

    # Добавление заголовков колонок
    for field in fields:
        tree.heading(field, text=field)
        tree.column(field, width=100)

    # Чтение данных из JSON-файла
    try:
        with open('_user.json', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

    # Добавление данных в таблицу
    for record in data:
        tree.insert('', 'end', values=[record.get(field, '') for field in fields])

    # Кнопка для закрытия окна
    close_btn = ttk.Button(database, text="Close", command=database.destroy)
    close_btn.pack(pady=20)

    database.mainloop()
# ----------

# -----Списки для динамического создания элементов-----
fields = ["Фамилия", "Имя", "Возраст", "Email", "Адрес"]
entries = {}

# -----Создание элементов-----
title = Label(window, text="Add a new person", font=("JetBrains mono", 20), foreground='green', justify='center', bg='lightblue')
add_person = ttk.Button(window, text="Add a new person", command=write_to_json)
clear_btn = ttk.Button(window, text='Clear', command=clear)
view_database_btn = ttk.Button(window, text='View Database', command=view_database)
written = Label(window, text='Person was successfully added!', fg='green', font=("JetBrains mono", 12))

# -----Расположение элементов-----
title.pack(pady=(0, 40))
add_person.place(relx=0.5, rely=1.0, anchor='s', width=130, height=40, y=-110)
clear_btn.place(relx=0.5, rely=1.0, anchor='s', width=130, height=40, y=-60)
view_database_btn.place(relx=0.5, rely=1.0, anchor='s', width=130, height=40, y=-10)
written.place_forget() # изначально текст об успешном добавлении скрыт

for field in fields:
    label = Label(window, text=f'{field}:', font=("JetBrains mono", 15))
    label.pack(pady=10)
    entry = ttk.Entry(window)
    entry.pack(pady=10)
    entries[field] = entry

# -----Главный цикл приложения-----
window.mainloop()
