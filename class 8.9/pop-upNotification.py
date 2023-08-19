import tkinter as tk
from tkinter import messagebox

def show_agreement():
    result = messagebox.askyesno("弹窗", "今天不写作业，你同意吗？")
    if result:
        window.destroy()
    else:
        show_agreement()

window = tk.Tk()
window.title("作业弹窗")

button = tk.Button(window, text="弹出作业弹窗", command=show_agreement)
button.pack(padx=20, pady=20)

window.mainloop()
