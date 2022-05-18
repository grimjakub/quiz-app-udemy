from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # self.window.config(width=500,height=500)

        self.label_score = Label(text="score: 0", bg=THEME_COLOR, font=("Arial", 15, "normal"), fg="white")
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text_question = self.canvas.create_text(150, 125, width=250, text="Some question",
                                                     font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        yes_img = PhotoImage(file="images/true.png")
        self.button_yes = Button(image=yes_img, command=self.yes_answer, highlightthickness=0)
        self.button_yes.grid(row=2, column=0)

        no_img = PhotoImage(file="images/false.png")
        self.button_no = Button(image=no_img, command=self.no_answer, highlightthickness=0)
        self.button_no.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=q_text)
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text_question, text="End of quiz")
            self.button_yes.config(state="disabled")
            self.button_no.config(state="disabled")

    def yes_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def no_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
