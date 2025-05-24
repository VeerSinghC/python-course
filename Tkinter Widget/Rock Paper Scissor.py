import tkinter as tk
import random

# Main game logic
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# GUI setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x250")

# Heading
title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

# Buttons for Rock, Paper, Scissors
rock_btn = tk.Button(window, text="Rock", width=15, command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(window, text="Paper", width=15, command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(window, text="Scissors", width=15, command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# Result display
result_label = tk.Label(window, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

window.mainloop()
