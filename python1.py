
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

score = 0
target_score = 10
history_list = []

root = ttk.Window(themename="superhero")
root.title("Counter App")
root.geometry("380x420")

def update_display():
    label_score.config(text=f"{score} / {target_score}")
    label_info.config(text=f"Mục tiêu hiện tại: {target_score} điểm")

def record_history(action):
    log_text = f"Điểm: {score}/{target_score} ({action})"
    history_list.append(log_text)
    listbox_history.insert(tk.END, log_text)
    listbox_history.yview(tk.END)

def set_target(new_target):
    global target_score, score
    target_score = new_target
    score = 0
    update_display()
    record_history(f"Đặt mục tiêu {new_target}")

def add_score():
    global score
    if score < target_score:
        score += 1
        update_display()
        record_history("+1")
        if score == target_score:
            messagebox.showinfo("Chúc mừng", f"Bạn đã hoàn thành mục tiêu {target_score} điểm!")

def subtract_score():
    global score
    if score > 0:
        score -= 1
        update_display()
        record_history("-1")

def reset_score():
    global score
    score = 0
    update_display()
    record_history("Reset")

label_score = tk.Label(root, text="0 / 10", font=("Arial", 22, "bold"))
label_score.pack(pady=8)

label_info = tk.Label(root, text="Mục tiêu hiện tại: 10 điểm", font=("Arial", 10))
label_info.pack(pady=4)

frame_targets = tk.Frame(root)
frame_targets.pack(pady=6)

label_target_title = tk.Label(frame_targets, text="Chọn mục tiêu: ", font=("Arial", 10))
label_target_title.grid(row=0, column=0, padx=4)

btn_t30 = tk.Button(frame_targets, text="30", width=4, bg="lightblue", command=lambda: set_target(30))
btn_t30.grid(row=0, column=1, padx=2)

btn_t10 = tk.Button(frame_targets, text="10", width=4, bg="lightblue", command=lambda: set_target(10))
btn_t10.grid(row=0, column=2, padx=2)

btn_t20 = tk.Button(frame_targets, text="50", width=4, bg="lightblue", command=lambda: set_target(50))
btn_t20.grid(row=0, column=3, padx=2)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=8)

btn_add = tk.Button(frame_buttons, text="+1", width=6, bg="lightgreen", command=add_score)
btn_add.grid(row=0, column=0, padx=4)

btn_sub = tk.Button(frame_buttons, text="-1", width=6, bg="lightcoral", command=subtract_score)
btn_sub.grid(row=0, column=1, padx=4)

btn_reset = tk.Button(frame_buttons, text="Reset", width=6, bg="lightyellow", command=reset_score)
btn_reset.grid(row=0, column=2, padx=4)

label_history = tk.Label(root, text="Lịch sử điểm:", font=("Arial", 10, "bold"))
label_history.pack(pady=(10, 2))

listbox_history = tk.Listbox(root, height=6, font=("Arial", 9))
listbox_history.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))

root.mainloop()