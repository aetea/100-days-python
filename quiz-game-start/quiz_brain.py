class QuizBrain():

    def __init__(self, questions) -> None:
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return True if self.question_number < len(self.question_list) else False

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(
            f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(response, curr_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it!")
        else:
            print(f"That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print()
