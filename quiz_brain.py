class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        # Retrieve current question
        question = self.question_list[self.question_number]
        question_text = question.text
        question_answer = question.answer

        # Increment the question number for display and next question
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        print(user_answer)
