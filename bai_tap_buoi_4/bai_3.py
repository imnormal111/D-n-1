import tkinter as tk

dem = 0

def tang_dem():
    global dem
    dem += 1
    label_dem.config(text=f"Đã bấm: {dem} lần")

root = tk.Tk()
root.title("Nút đếm")
root.geometry("300x180")

btn_dem = tk.Button(root, text="Bấm vào tôi", command=tang_dem, font=("Arial", 11))
btn_dem.pack(pady=20)

label_dem = tk.Label(root, text="Đã bấm: 0 lần", font=("Arial", 12))
label_dem.pack(pady=10)

root.mainloop()