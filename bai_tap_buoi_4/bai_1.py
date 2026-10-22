import tkinter as tk

def doi_chu():
    label.config(text="Đã bấm!")

root = tk.Tk()
root.title("Nút đổi chữ")
root.geometry("300x150")

label = tk.Label(root, text="Chưa bấm", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Bấm vào đây", command=doi_chu, font=("Arial", 10))
btn.pack()

root.mainloop()