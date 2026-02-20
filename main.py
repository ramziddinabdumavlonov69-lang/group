import tkinter as tk
from tkinter import filedialog, messagebox
from brain import process_input
from memory import Memory
from file_manager import save_file

memory = Memory()

def send():
    user_text = entry.get()
    if not user_text:
        return

    response = process_input(user_text)

    chat.insert(tk.END, "Siz: " + user_text + "\n")
    chat.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

def upload_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        filename = save_file(filepath)
        memory.add_memory("file", filename)
        messagebox.showinfo("Fayl", "Fayl saqlandi!")

def show_all():
    chat.delete(1.0, tk.END)
    for item in memory.get_all_memories():
        chat.insert(tk.END, f"{item[0]} | {item[1]} | {item[2]}\n")

root = tk.Tk()
root.title("Smart Memory Bot")
root.geometry("600x600")

chat = tk.Text(root, height=20, width=70)
chat.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Yuborish", command=send).pack(pady=5)
tk.Button(root, text="Fayl yuklash", command=upload_file).pack(pady=5)
tk.Button(root, text="Bazani ko‘rish", command=show_all).pack(pady=5)

root.mainloop()
