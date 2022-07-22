from tkinter import *

THEME_COLOR = "#375362"


class Menu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzlereczek")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label_score = Label(text="Score:", bg=THEME_COLOR, fg='white')
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, text="Ello Byuu ", font=("Ariel", 20, "bold"),
                                                   fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.yes_image = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=self.yes_image, highlightthickness=0, bg=THEME_COLOR)
        self.button_yes.grid(row=2, column=0)

        self.no_image = PhotoImage(file="images/false.png")
        self.button_yes = Button(image=self.no_image, highlightthickness=0, bg=THEME_COLOR)
        self.button_yes.grid(row=2, column=1)

        self.window.mainloop()
