import tkinter as tk

def tinh_tong():
    so1 = float(entry1.get())
    so2 = float(entry2.get())
    label_ket_qua.config(text=f"Tổng: {so1 + so2}")

root = tk.Tk()
root.title("Cộng")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

btn = tk.Button(root, text="Tính tổng", command=tinh_tong)
btn.pack(pady=5)

label_ket_qua = tk.Label(root, text="")
label_ket_qua.pack(pady=5)

root.mainloop()