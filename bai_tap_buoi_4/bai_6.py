

import tkinter as tk

def doi_mau():
    root.config(bg="lightblue")

root = tk.Tk()
root.title("Nút đổi màu")
root.geometry("300x200")

btn = tk.Button(root, text="Đổi màu nền", command=doi_mau)
btn.pack(pady=50)

root.mainloop()


import tkinter as tk

def tinh_cong():
    so1 = float(entry1.get())
    so2 = float(entry2.get())
    label_ket_qua.config(text=f"Cộng: {so1 + so2} / Trừ: {so1 - so2}") # Hoặc chỉ hiện kết quả cộng

def tinh_cong():
    so1 = float(entry1.get())
    so2 = float(entry2.get())
    label_ket_qua.config(text=f"Cộng: {so1 + so2}")

def tinh_tru():
    so1 = float(entry1.get())
    so2 = float(entry2.get())
    label_ket_qua.config(text=f"Trừ: {so1 - so2}")

root = tk.Tk()
root.title("Máy tính cộng/trừ")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

btn_cong = tk.Button(root, text="Cộng", command=tinh_cong)
btn_cong.pack(pady=2)

btn_tru = tk.Button(root, text="Trừ", command=tinh_tru)
btn_tru.pack(pady=2)

label_ket_qua = tk.Label(root, text="")
label_ket_qua.pack(pady=5)

root.mainloop()