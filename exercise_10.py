from multiple_choice import Choice

def askUser(prompt):
    prompt.display()
    userAnswer = input("Your answer: ")
    print()
    print(prompt.check_answer(userAnswer), "\n")


def main():
    first_question = Choice()
    first_question.ask_question("1 x 1")
    first_question.add_choice("0", False)
    first_question.add_choice("-1", True)
    first_question.add_choice("1", False)
    first_question.add_choice("11", False)

    second_question = Choice()
    second_question.ask_question("12 x 12")
    second_question.add_choice("96", False)
    second_question.add_choice("122", False)
    second_question.add_choice("14", False)
    second_question.add_choice("144", True)

    third_question = Choice()
    third_question.ask_question("15 x 3")
    third_question.add_choice("15", False)
    third_question.add_choice("35", False)
    third_question.add_choice("45", True)
    third_question.add_choice("23", False)

    fourth_question = Choice()
    fourth_question.ask_question("6 x 9")
    fourth_question.add_choice("54", True)
    fourth_question.add_choice("69", False)
    fourth_question.add_choice("96", False)
    fourth_question.add_choice("37", False)

    fifth_question = Choice()
    fifth_question.ask_question("8 x 25")
    fifth_question.add_choice("225", False)
    fifth_question.add_choice("400", False)
    fifth_question.add_choice("200", True)
    fifth_question.add_choice("175", False)

    askUser(first_question)
    askUser(second_question)
    askUser(third_question)
    askUser(fourth_question)
    askUser(fifth_question)



main()