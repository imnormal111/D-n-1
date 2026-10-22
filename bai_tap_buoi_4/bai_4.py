import tkinter as tk

def tinh_binh_phuong():
    so = float(entry_so.get())
    label_ket_qua.config(text=f"Bình phương: {so * so}")

root = tk.Tk()
root.title("Bình phương")
root.geometry("300x150")

# Ô nhập liệu
entry_so = tk.Entry(root)
entry_so.pack(pady=5)

# Nút tính toán
btn = tk.Button(root, text="Tính", command=tinh_binh_phuong)
btn.pack(pady=5)

# Nhãn hiển thị kết quả
label_ket_qua = tk.Label(root, text="")
label_ket_qua.pack(pady=5)

root.mainloop()