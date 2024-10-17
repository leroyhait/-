import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Тир в слепую')
root.geometry('800x600')

target_radius = 50
target_position = (0, 0)
score = 0

def generate_target():
    global target_position
    canvas.delete("target")
    window_width = canvas.winfo_width()
    window_height = canvas.winfo_height()
    if window_width > 2 * target_radius and window_height > 2 * target_radius:
        x = random.randint(target_radius, window_width - target_radius)
        y = random.randint(target_radius, window_height - target_radius)
        target_position = (x, y)
    else:
        print("Ошибка")

def check_hit(event):
    global score
    x, y = event.x, event.y
    target_x, target_y = target_position
    distance = ((x - target_x) ** 2 + (y - target_y) ** 2) ** 0.5
    if distance <= target_radius:
        score += 1
        score_label.config(text=f"Очки: {score}")
        hint_label.config(text="Попал!")
        generate_target()
    else:
        give_hint(x, y)

def give_hint(x, y):
    target_x, target_y = target_position
    hint = ""
    if y < target_y:
        hint += "Ниже "
    elif y > target_y:
        hint += "Выше "

    if x < target_x:
        hint += "Правее "
    elif x > target_x:
        hint += "Левее "

    hint_label.config(text=hint)

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

score_label = tk.Label(root, text=f"Очки: {score}", font=('Arial', 14))
score_label.pack(side=tk.LEFT, padx=10)

hint_label = tk.Label(root, text="", font=('Arial', 12), fg="red")
hint_label.pack(side=tk.BOTTOM, pady=10)

root.after(500, generate_target)
canvas.bind('<Button-1>', check_hit)
root.mainloop()