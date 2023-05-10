import tkinter as tk
import pandas as pd
import pickle

# Создание переменных для хранения данных
data = pd.DataFrame(columns=["Название файла", "Назначение", "Местоположение"])

# Создание функции для добавления новых записей
def add_row():
    # Считывание данных из полей ввода
    file_name = file_name_entry.get()
    purpose = purpose_entry.get()
    location = location_entry.get()
    
    # Добавление новой строки в DataFrame
    data.loc[len(data)] = [file_name, purpose, location]
    
    # Обновление таблицы в графическом интерфейсе
    update_table()

# Создание функции для обновления таблицы
def update_table():
    # Удаление предыдущей таблицы (если она есть)
    for widget in table_frame.winfo_children():
        widget.destroy()
    
    # Создание новой таблицы на основе DataFrame
    for i, row in data.iterrows():
        file_name_label = tk.Label(table_frame, text=row["Название файла"])
        file_name_label.grid(row=i, column=0)
        
        purpose_label = tk.Label(table_frame, text=row["Назначение"])
        purpose_label.grid(row=i, column=1)
        
        location_label = tk.Label(table_frame, text=row["Местоположение"])
        location_label.grid(row=i, column=2)

# Создание функции для сохранения данных в файл
def save_data():
    with open("data.pickle", "wb") as f:
        pickle.dump(data, f)

# Создание функции для загрузки данных из файла
def load_data():
    global data
    try:
        with open("data.pickle", "rb") as f:
            data = pickle.load(f)
    except FileNotFoundError:
        pass
    
    # Обновление таблицы в графическом интерфейсе
    update_table()

# Создание графического интерфейса
root = tk.Tk()
root.title("Таблица файлов")

# Создание полей ввода и кнопки для добавления записей
file_name_label = tk.Label(root, text="Название файла:")
file_name_label.pack()
file_name_entry = tk.Entry(root)
file_name_entry.pack()

purpose_label = tk.Label(root, text="Назначение:")
purpose_label.pack()
purpose_entry = tk.Entry(root)
purpose_entry.pack()

location_label = tk.Label(root, text="Местоположение:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

add_button = tk.Button(root, text="Добавить", command=add_row)
add_button.pack()

# Создание фрейма для таблицы
table_frame = tk.Frame(root)
table_frame.pack()

# Создание кнопок для сохранения и загрузки данных
save_button = tk.Button(root, text="Сохранить", command=save_data)
save_button.pack()

load_button = tk.Button(root, text="Загрузить", command=load_data)
load_button.pack()

# Вывод таблицы при запуске программы
load_data()

# Запуск интерфейса
root.mainloop()
