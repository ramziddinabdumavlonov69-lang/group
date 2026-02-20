import tkinter as tk
from tkinter import messagebox
from memory import Memory

memory = Memory()

def add():
    text = entry.get()
    if text:
        memory.add_memory(text)
        messagebox.showinfo("Saqlash", "Ma'lumot saqlandi!")
        entry.delete(0, tk.END)
        show_all()

def search():
    keyword = entry.get()
    result = memory.search_memory(keyword)
    listbox.delete(0, tk.END)
    for item in result:
        listbox.insert(tk.END, f"{item[0]}: {item[1]}")

def show_all():
    listbox.delete(0, tk.END)
    for item in memory.get_all_memories():
        listbox.insert(tk.END, f"{item[0]}: {item[1]}")

def delete():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        memory_id = selected.split(":")[0]
        memory.delete_memory(memory_id)
        show_all()

root = tk.Tk()
root.title("Saqlovchi Bot")
root.geometry("500x500")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Saqlash", command=add).pack(pady=5)
tk.Button(root, text="Qidirish", command=search).pack(pady=5)
tk.Button(root, text="Hammasini ko‘rsat", command=show_all).pack(pady=5)
tk.Button(root, text="O‘chirish", command=delete).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=15)
listbox.pack(pady=10)

show_all()

root.mainloop()
