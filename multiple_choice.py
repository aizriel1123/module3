class Question:
    def __init__(self):
        self._question = ""
        self._answer = ""

    def ask_question(self, question_text):
        self._question = question_text + "?\n----------------"

    def give_answer(self, question_answer):
        self._answer = question_answer

    def check_answer(self, user_answer):
        return user_answer == self._answer

    def display(self):
        print(self._question)


class Choice(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def add_choice(self, choice, correct_choice):
        self._choices.append(choice)
        if correct_choice:
            answer_position = str(len(self._choices))
            self.give_answer(answer_position)

    def display(self):
        super().display()

        for i in range(len(self._choices)):
            position = i + 1
            print("%d: %s" % (position, self._choices[i]))


