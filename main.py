from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Initialize empty question list
question_bank = []

# Loop question data to create question list with list of questions objects
for question in question_data:
    text = question['text']
    answer = question['answer']
    question_obj = Question(text, answer)
    question_bank.append(question_obj)

q1 = QuizBrain(question_bank)

while q1.still_has_questions():
    q1.next_question()
