from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text=q_text, q_answer=q_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")