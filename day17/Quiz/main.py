from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_obj=Question(question["text"],question["answer"])
    question_bank.append(question_obj)

quiz=QuizBrain(question_bank)

while quiz.stil_has_questions():
    quiz.next_question()

print("You've Completed the quiz")
print(f"Your final Score Was:- {quiz.score}/{quiz.question_number}")