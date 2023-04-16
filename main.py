from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create a question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create the quiz
quiz = QuizBrain(question_bank)

# Do the questions
while quiz.still_has_questions():
    quiz.next_question()

# At end of the quiz, report the score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
