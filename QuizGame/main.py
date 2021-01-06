from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in range(len(question_data)):
    element = question_data[x]
    question_bank.append(Question(element['text'], element['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()