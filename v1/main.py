from constants import questions, topics

global marks

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
    tries = 0

    for question in question_list:
        print("Question: " + question["question"])
        print("Options: " + question["options"])
        answer = input("Enter your answer: ").lower()

        if question["type"] != "order":
            tries += 1

            while answer != question["answer"].lower():
                if tries == 1:
                    print("Hint: " + question["hint"])
                    answer = input("Enter your answer: ").lower()
                else:
                    answer = input("Incorrect! Re-enter your answer: ").lower()

                tries +=1
                earned_marks = get_marks(tries, question["type"])

            marks += earned_marks
            print("Correct! " + question["message"])
            print(f"You earned a total of {earned_marks} marks.")

def choose_topic():
    selection = input("Choose a topic: dynamics, speed and tempo, beats or time signature and clef").lower()
    topic = questions[topics[selection]]

    while not topic:
        selection = input("Please choose a valid topic: dynamics, speed and tempo, beats or time signature and clef").lower()
        topic = questions[topics[selection]]

    run_questions(topic["questions"])

    choose_next = input("Would you like to do anothe")   
