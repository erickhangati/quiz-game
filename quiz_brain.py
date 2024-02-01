class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        """
        Checks if there are more questions to answer
        :return: boolean
        """
        return self.question_number <= len(self.question_list) - 1

    def next_question(self):
        """
        Prompts the user with questions and invoke the check answer method wit the answer.
        :return: None
        """
        # Retrieve current question
        question = self.question_list[self.question_number]
        question_text = question.text
        question_answer = question.answer

        # Increment the question number for display and next question
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")

        # Check answer
        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks if user answer is correct and prints score.
        :param user_answer: answer from the user
        :param correct_answer: correct answer from the question data.
        :return: None
        """
        if user_answer.lower() == correct_answer.lower():
            # Increment the score
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
