import tkinter as tk
from tkinter import ttk
import sqlite3

class TodoList:
    def __init__(self, master):
        self.master = master
        master.title("Todo List")

        # создаем окно
        self.frame = tk.Frame(master)
        self.frame.pack()

        # создаем таблицу
        self.table = tk.ttk.Treeview(self.frame, columns=('employee', 'task'), show='headings')
        self.table.heading('employee', text='Сотрудник')
        self.table.heading('task', text='Задача')
        self.table.column('employee', width=150)
        self.table.column('task', width=200)
        self.table.pack()

        # создаем кнопки управления задачами
        self.add_button = tk.Button(self.frame, text='Добавить задачу', command=self.add_task)
        self.add_button.pack(side='left', padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text='Сохранить задачи', command=self.save_tasks)
        self.save_button.pack(side='left', padx=5, pady=5)

        self.load_button = tk.Button(self.frame, text='Загрузить задачи', command=self.load_tasks)
        self.load_button.pack(side='left', padx=5, pady=5)

        # создаем базу данных
        self.conn = sqlite3.connect('todo_list.db')
        self.cur = self.conn.cursor()

        # создаем таблицу задач, если ее нет
        self.cur.execute('''CREATE TABLE IF NOT EXISTS tasks
                            (employee TEXT, task TEXT)''')
        self.conn.commit()

        # загружаем задачи из базы данных
        self.load_tasks()

    def add_task(self):
        # создаем диалоговое окно для ввода задачи
        dialog = tk.Toplevel()
        dialog.title('Добавить задачу')

        # создаем поля ввода для сотрудника и задачи
        employee_label = tk.Label(dialog, text='Сотрудник:')
        employee_label.pack()
        employee_entry = tk.Entry(dialog)
        employee_entry.pack()

        task_label = tk.Label(dialog, text='Задача:')
        task_label.pack()
        task_entry = tk.Entry(dialog)
        task_entry.pack()

        # создаем кнопку добавления задачи
        add_button = tk.Button(dialog, text='Добавить', command=lambda: self.add_task_confirm(dialog, employee_entry.get(), task_entry.get()))
        add_button.pack(pady=5)

    def add_task_confirm(self, dialog, employee, task):
        # добавляем задачу в базу данных
        self.cur.execute('INSERT INTO tasks VALUES (?, ?)', (employee, task))
        self.conn.commit()

        # добавляем задачу в таблицу
        self.table.insert('', 'end', values=(employee, task))

        # закрываем диалоговое окно
        dialog.destroy()

    def save_tasks(self):
        # сохраняем задачи в файл todo_list.txt
        tasks = self.table.get_children()
        with open('todo_list.txt', 'w') as f:
            for t in tasks:
                employee, task = self.table.item(t)['values']
                f.write('{} - {}\n'.format(employee, task))

    def load_tasks(self):
        # очищаем таблицу
        self.table.delete(*self.table.get_children())

        # загружаем задачи из базы данных
        self.cur.execute('SELECT * FROM tasks')
        rows = self.cur.fetchall()
        for row in rows:
            self.table.insert('', 'end', values=row)
  
root = tk.Tk()
todo_list = TodoList(root)
root.mainloop()