from question_model import Question
from data import question_data, external_questions
from quiz_brain import QuizBrain

question_bank = []
for question in external_questions:
    question_text = question.get("question", None)
    question_answer = question.get("correct_answer", None)
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for r in question_bank:  # Debug Code
#     print(f"text: {r.text}, answer: {r.answer}")  # Debug Code

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz.")
print(f"You're final score is {quiz.score}/{quiz.question_number}.")