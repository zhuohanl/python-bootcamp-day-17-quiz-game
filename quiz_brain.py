class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        :return: A boolean depending on the value of question_number
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieve the item at the current question_number from the question_list.
        Use the input() function to show the user the Question text and ask for the user's answer.

        :return: user's input of answer
        """
        # question_number stays 0 as we need 0 here
        current_question = self.question_list[self.question_number]

        # we need the question_number to be shown as 1
        # also we need to increase the number each time
        self.question_number += 1

        # get the user answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

        # compare if the user answer is the same as the question answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
