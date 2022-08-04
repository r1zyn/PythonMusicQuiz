from constants import questions, topics, topic_list

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
            return 5
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

        if question["type"] != "order":
            answer = input("Enter your answer: ").lower()

            while not answer in question["options"]:
                answer = input("Invalid answer - please try again: ").lower()

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
            print("Hint: " + question["hint"])

            answer = input("Enter your answer: ").lower()
            correct_places = 0
            option_amount = len(question["answer"])

            while answer.find(", ") == -1:
                answer = input("Invalid format - please try again: ").lower()

            for i in range(option_amount):
                if answer.split(", ")[i] == question["answer"][i]:
                    correct_places += 1

            earned_marks = get_marks(type=question["type"], correct_places=correct_places)
            marks += earned_marks
            print("You completed the question with " + str(correct_places) + " correct places. " + question["message"])
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks.")

    return marks

def init():
    selection = input("Choose a topic: dynamics, speed and tempo, beats or time signature and clef\nYour selection: ").lower()

    while not selection in topic_list:
        selection = input("Please choose a valid topic: dynamics, speed and tempo, beats or time signature and clef\nYour selection: ").lower()

    topic = questions[topics[selection]]
    marks = run_questions(topic["questions"])

    run_next = input(f"Would you like to do another topic? (y/n)\n").lower()
    if run_next == "y" or run_next == "yes":
        topic = init()
        marks = run_questions(topic["questions"])
    else: 
        print(f"Cancelled topic selection. Thanks for playing! You earned a total of {marks} marks.")

init()