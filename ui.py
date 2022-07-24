from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterFace:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzlereczek")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label_score = Label(text=f"Score:", bg=THEME_COLOR, fg='white')
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg='white', highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=200, text="Ello Byuu ", font=("Ariel", 10, "bold"),
                                                   fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.yes_image = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=self.yes_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.button_yes.grid(row=2, column=0)

        self.no_image = PhotoImage(file="images/false.png")
        self.button_no = Button(image=self.no_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.button_no.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="End game")
            self.button_yes.config(state='disable')
            self.button_no.config(state='disable')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def end_quiz(self):
        pass
