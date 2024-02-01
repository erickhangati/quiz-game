from data import question_data
from question_model import Question

# Initialize empty question list
question_bank = []

# Loop question data to create question list with list of questions objects
for question in question_data:
    text = question['text']
    answer = question['answer']
    question_obj = Question(text, answer)
    question_bank.append(question_obj)

