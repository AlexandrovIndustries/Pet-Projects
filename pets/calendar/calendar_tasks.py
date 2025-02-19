import json
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = entry.get()
    if task:
        date = calendar.get_date()
        tasks = load_tasks()
        if date not in tasks:
            tasks[date] = []
        tasks[date].append({"task": task, "done": False})
        save_tasks(tasks)
        entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Ошибка", "Введите текст задачи!")

def update_task_list():
    listbox.delete(0, tk.END)
    date = calendar.get_date()
    tasks = load_tasks()
    if date in tasks:
        for i, task in enumerate(tasks[date], 1):
            status = "[x]" if task["done"] else "[ ]"
            listbox.insert(tk.END, f"{i}. {status} {task['task']}")

def mark_done():
    try:
        index = listbox.curselection()[0]
        date = calendar.get_date()
        tasks = load_tasks()
        tasks[date][index]["done"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        date = calendar.get_date()
        tasks = load_tasks()
        tasks[date].pop(index)
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу!")

def on_date_select(event):
    update_task_list()

def main():
    global entry, listbox, calendar
    root = tk.Tk()
    root.title("Календарь задач")
    
    
    calendar = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.pack(pady=10)
    calendar.bind("<<CalendarSelected>>", on_date_select)

  
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    entry = tk.Entry(frame, width=40)
    entry.pack(side=tk.LEFT, padx=5)
    
    add_button = tk.Button(frame, text="Добавить", command=add_task)
    add_button.pack(side=tk.RIGHT)
    
 
    listbox = tk.Listbox(root, width=50, height=10)
    listbox.pack(pady=10)
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)
    
    done_button = tk.Button(button_frame, text="Отметить выполненным", command=mark_done)
    done_button.pack(side=tk.LEFT, padx=5)
    
    delete_button = tk.Button(button_frame, text="Удалить", command=delete_task)
    delete_button.pack(side=tk.RIGHT, padx=5)
    
    update_task_list()
    
    root.mainloop()

if __name__ == "__main__":
    main()
