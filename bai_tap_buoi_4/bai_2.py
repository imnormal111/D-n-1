import tkinter as tk

def chao_hoi():
    ten = entry_ten.get()
    if ten.strip() == "":
        label_ket_qua.config(text="Vui lòng nhập tên!")
    else:
        label_ket_qua.config(text=f"Xin chào, {ten}!")

root = tk.Tk()
root.title("hello")
root.geometry("350x200")

tk.Label(root, text="Nhập tên của bạn:", font=("Arial", 10)).pack(pady=5)
entry_ten = tk.Entry(root, font=("Arial", 11), width=20)
entry_ten.pack(pady=5)

btn_chào = tk.Button(root, text="Chào", command=chao_hoi, font=("Arial", 10))
btn_chào.pack(pady=5)

label_ket_qua = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_ket_qua.pack(pady=10)

root.mainloop()