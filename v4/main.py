from time import sleep
from constants import questions, topics, topic_list
from re import search

def get_marks(tries = 0, type = "", correct_places = 0):
    if type.lower() == "multichoice" or type.lower() == "word":
        if tries == 1:
            return 10
        elif tries == 2:
            return 5
        elif tries == 3:
            return 3
        elif tries == 4:
            return 1
        else:
            return 0
    elif type.lower() == "true/false":
        if tries == 1:
            return 10
        elif tries == 2:
            return 1
        else:
            return 0
    elif type.lower() == "order":
        if correct_places == 4:
            return 10
        elif correct_places == 3:
            return 5
        elif correct_places == 2:
            return 3
        elif correct_places == 1:
            return 1
        else: 
            return 0

def run_questions(question_list):
    marks = 0
    earned_marks = 0
    tries = 0

    for question in question_list:
        print("Question: " + question["question"])
        print("Options:\n" + question["option_string"])

        if question["type"] == "order":
            print("Hint: " + question["hint"])

            answer = input("Enter your answer: ").lower()
            correct_places = 0
            option_amount = len(question["answer"])
            matches = search("^(\d\,\s){3}\d$", answer)

            while matches == None:
                answer = input("Invalid format, please try again: ").lower()

            for i in range(option_amount):
                if answer.split(", ")[i] == question["answer"][i]:
                    correct_places += 1

            earned_marks = get_marks(type=question["type"], correct_places=correct_places)
            marks += earned_marks
            print("You completed the question with " + str(correct_places) + " correct places. " + question["message"])
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks.")
        elif question["type"] == "word":
            answer = input("Enter your answer: ").lower()

            tries += 1

            while answer != question["answer"].lower():
                if tries == 1:
                    print("Hint: " + question["hint"])
                    answer = input("Enter your answer: ").lower()
                else:
                    answer = input("Incorrect! Re-enter your answer: ").lower()

                tries += 1

            earned_marks = get_marks(tries=tries, type=question["type"])
            marks += earned_marks
            print("Correct! " + question["message"])
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks.")
        else:
            answer = input("Enter your answer: ").lower()

            while not answer in question["options"]:
                answer = input("Invalid answer, please try again: ").lower()

            tries += 1

            while answer != question["answer"].lower():
                if tries == 1:
                    print("Hint: " + question["hint"])
                    answer = input("Enter your answer: ").lower()
                else:
                    answer = input("Incorrect! Re-enter your answer: ").lower()

                tries += 1

            earned_marks = get_marks(tries=tries, type=question["type"])
            marks += earned_marks
            print("Correct! " + question["message"])
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks.")

        tries = 0
        sleep(2)

    return marks

def run_selection():
    selection = input("Choose a topic: dynamics, speed and tempo, beats or time signature, clef, all\nYour selection: ").lower()

    while not selection in topic_list:
        selection = input("Please choose a valid topic: dynamics, speed and tempo, beats or time signature and clef\nYour selection: ").lower()

    topic = questions[topics[selection]]
    marks = 0

    if selection == "all" or all:
        for topic in topic_list:
            marks += run_questions(topic["questions"])

        print(f"Thanks for playing! You earned a total of {marks} marks.")
    else:
        marks = run_questions(topic["questions"])
        print(f"Thanks for playing! You earned a total of {marks} marks.")

    run_next = input(f"Would you like to do another topic? (y/n)\n").lower()
    if run_next == "y" or run_next == "yes":
        run_selection()
    else: 
        exit(0)

def init():
    print("-----------[ Python Music Quiz ]-----------")
    print("Welcome to the Python music quiz! This is a music quiz written in Python to help you user prepare for music theories ranging from 4 different topics:")
    print(" » Dynamics\n » Speed and tempo\n » Beats\n » Time signature and clef\n")
    print("You will receive a variety of type of questions in each topic: ")
    print(" » Multiple choice questions\n   1st try: 10 marks\n   2nd try: 5 marks\n   3rd try: 3 marks\n   4th try: 1 mark\n")
    print(" » Word questions\n   1st try: 10 marks\n   2nd try: 5 marks\n   3rd try: 3 marks\n   4th try: 1 mark\n")
    print(" » True/False questions\n   1st try: 10 marks\n   2nd try: 1 mark\n")
    print(" » Order questions\n   4 correct places: 10 marks\n   3 correct places: 5 marks\n   2 correct places: 3 marks\n   1 correct place: 1 mark\n")
    print("You will receive one hint after your first try for every question.")
    print("Note: there will be 2 second delay after every question.")

    run_selection()

init()