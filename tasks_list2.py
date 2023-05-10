import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.title("Список задач")

        # Создаем таблицу для задач
        self.table = ttk.Treeview(self.master, columns=('employee', 'task'), show='headings')
        self.table.heading('employee', text='Сотрудник')
        self.table.heading('task', text='Задача')
        self.table.pack(fill='both', expand=True)

        # Создаем окно для добавления задачи
        self.employee_var = tk.StringVar()
        self.task_var = tk.StringVar()
        self.add_window = tk.Toplevel(self.master)
        tk.Label(self.add_window, text="Сотрудник").grid(row=0, column=0)
        tk.Entry(self.add_window, textvariable=self.employee_var).grid(row=0, column=1)
        tk.Label(self.add_window, text="Задача").grid(row=1, column=0)
        tk.Entry(self.add_window, textvariable=self.task_var).grid(row=1, column=1)
        tk.Button(self.add_window, text="Добавить", command=self.add_task).grid(row=2, column=1)

        # Создаем меню
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Добавить задачу", command=self.show_add_window)
        file_menu.add_command(label="Удалить задачу", command=self.delete_task)
        file_menu.add_separator()
        file_menu.add_command(label="Сохранить", command=self.save_file)
        file_menu.add_command(label="Загрузить", command=self.load_file)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.master.config(menu=menu_bar)

    def show_add_window(self):
        self.add_window.deiconify()

    def hide_add_window(self):
        self.add_window.withdraw()

    def add_task(self):
        employee = self.employee_var.get()
        task = self.task_var.get()
        self.table.insert("", "end", values=(employee, task))
        self.hide_add_window()

    def delete_task(self):
        selected_item = self.table.selection()[0]
        self.table.delete(selected_item)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file_path:
            return
        with open(file_path, 'w') as f:
            for item in self.table.get_children():
                f.write(", ".join(self.table.item(item)['values']) + "\n")

    def load_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        if not file_path:
            return
        with open(file_path, 'r') as f:
            for line in f:
                values = line.strip().split(", ")
                self.table.insert("", "end", values=values)


if __name__ == '__main__':
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()