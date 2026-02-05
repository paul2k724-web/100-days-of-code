import requests
from tkinter import Tk, Label, Button

# ---------------- API ----------------
response = requests.get(
    "https://opentdb.com/api.php",
    params={"amount": 5, "type": "boolean"}
)
response.raise_for_status()
question_data = response.json()["results"]

# ---------------- QUESTION MODEL ----------------
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = [
    Question(q["question"], q["correct_answer"])
    for q in question_data
]

# ---------------- QUIZ LOGIC ----------------
class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions

    def has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        q = self.questions[self.question_number]
        self.question_number += 1
        return q.text

    def check_answer(self, user_answer):
        correct = self.questions[self.question_number - 1].answer
        if user_answer == correct:
            self.score += 1
            return True
        return False

quiz = QuizBrain(question_bank)

# ---------------- UI ----------------
window = Tk()
window.title("Quiz App")

question_label = Label(text="", wraplength=300, font=("Arial", 14))
question_label.pack(pady=20)

score_label = Label(text="Score: 0")
score_label.pack()

def get_next_question():
    if quiz.has_questions():
        question_label.config(text=quiz.next_question())
    else:
        question_label.config(text="Quiz completed!")
        true_button.config(state="disabled")
        false_button.config(state="disabled")

def true_pressed():
    if quiz.check_answer("True"):
        score_label.config(text=f"Score: {quiz.score}")
    get_next_question()

def false_pressed():
    if quiz.check_answer("False"):
        score_label.config(text=f"Score: {quiz.score}")
    get_next_question()

true_button = Button(text="True", command=true_pressed)
true_button.pack(side="left", padx=20)

false_button = Button(text="False", command=false_pressed)
false_button.pack(side="right", padx=20)

get_next_question()
window.mainloop()
