import secrets
import tkinter as tk

root = tk.Tk()
root.title("Game")
root.geometry("800x500")

entry = tk.Entry(root, bd=5)
entry.place(x=460, y=90)
liststring = ['Eight', 'Yellow', 'Expensive', 'Seven']
listPlayer = ["player1", "player2", "player3", "player4"]
listQuestion = ["How many planets are in our solar system?", "What is the color of a school bus?",
                "What is the opposite of ‘cheap’?", "How many continents are there in the world?"]


def call():
    etext = entry.get()
    x = 0
    if etext in liststring:
        print("yes")
        lab = tk.Label(root, text="Correct Answer")
        lab.place(x=610, y=40)
    else:
        print("No")
        lab1 = tk.Label(root, text="Wrong Answer!")
        lab1.place(x=610, y=40)
        listPlayer.pop(x)
        displayPlayer(listPlayer)


def displayPlayer(p=None):
    if p is None:
        p = []
    x = 0
    q = 90
    while x < len(p):
        lab = tk.Label(root, text=p[x])
        lab.place(x=640, y=q)
        q = q + 19
        x = x + 1
        if x == 4:
            break


button = tk.Button(root, text="Ok", command=lambda: [call()])
button.place(x=600, y=90)

nextButton = tk.Button(root, text="Next Question")
backButton = tk.Button(root, text="Last Question")
print("Random element is :", secrets.choice(listQuestion))
nextButton.place(x=590, y=460)
backButton.place(x=390, y=460)
displayPlayer(listPlayer)
root.mainloop()
