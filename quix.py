#made by abraham paul sanhith
# ---------- QUESTION CLASS ----------
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
#made by abraham paul sanhith

# ---------- QUIZ BRAIN CLASS ----------
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


# ---------- QUESTION DATA ----------
question_data = [
    {"text": "Python is a programming language.", "answer": "True"},
    {"text": "The Sun revolves around the Earth.", "answer": "False"},
    {"text": "2 + 2 equals 4.", "answer": "True"},
    {"text": "Fish can fly naturally.", "answer": "False"},
]

# ---------- CREATE QUESTION OBJECTS ----------
question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

# ---------- START QUIZ ----------
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Final score: {quiz.score}/{quiz.question_number}")
