from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("quiz finished!")
print(f"your total score is {quiz.score}/{len(question_bank)}")
