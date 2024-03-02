"""Simple popular game rock paper scissors with simple gui"""

import random
import tkinter as tk

def play(userInput):
    akcje = ["nożyce", "papier", "kamień"]
    computer_action = random.choice(akcje)

    if computer_action == userInput:
        result_label.config(text=f"Oboje wybraliście {computer_action}. To jest remis!")
    elif(computer_action=="nożyce" and userInput=="papier") or (computer_action=="kamień" and userInput=="nożyce") or (computer_action=="papier" and userInput=="kamień"):
        result_label.config(text=f"Komputer wygrał bo pokazał: {computer_action} a ty: {userInput}")
    else:
        result_label.config(text=f"Ty wygrałeś bo pokazałeś: {userInput} a komputer: {computer_action}")


def choice_scissors():
    play("nożyce")
    print("Użytkownik wybrał nożyce!")

def choice_paper():
    play("papier")
    print("Użytkownik wybrał papier!")

def choice_rock():
    play("kamień")
    print("Użytkownik wybrał kamień!")





root = tk.Tk()
frame = tk.Frame(root)
root.title("Gra w nożyce, papier, kamień")
frame.pack()
frame.pack(expand=True, fill=tk.BOTH)
root.geometry("300x300")
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
#button.pack(side=tk.BOTTOM)
button.pack(side=tk.BOTTOM, padx=5, pady=5, expand=True, fill=tk.BOTH)

result_label = tk.Label(frame, text="")
result_label.pack(pady=10)



button1=tk.Button(frame,text="Nożyce",command=choice_scissors)
#button1.pack(side=tk.RIGHT)
button1.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

button2=tk.Button(frame,text="Papier",command=choice_paper)
button2.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)
#button2.pack(side=tk.RIGHT)

button3=tk.Button(frame,text="Kamień",command=choice_rock)
button3.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)
#button3.pack(side=tk.RIGHT)


root.mainloop()
