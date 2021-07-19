from question_model import Question
from data import question_data, question_data_new
from quiz_brain import QuizBrain

# question_bank = [Question(q["text"], q["answer"]) for q in question_data]
question_bank = [Question(q["question"], q["correct_answer"])
                 for q in question_data_new]

# print(question_bank[1])

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("~ ~ ~ Quiz complete! ~ ~ ~")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
