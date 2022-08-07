def get_marks(tries = 0, type = "", correct_places = 0):
    if type == "multichoice" or type == "word":
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
    elif type == "true/false":
        if tries == 1:
            return 10
        elif tries == 2:
            return 5
        else:
            return 0
    elif type == "order":
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

def run_questions(topic):
    tries = 0
    marks = 0

    if topic == "dynamics":
        print("What does a crescendo mean? (Choose from a, b, c or d)")
        print("a) Getting louder\nb) Getting quiter\nc) Getting faster\nd) Getting slower")
        answer = input("Your answer: ")
        tries += 1

        while answer != "a":
            if tries == 1:
                print("Hint: It is similar to the english definition.")
                answer = input("Your answer: ")
                tries += 1
            else:
                answer = input("Incorrect! Re-enter your answer: ")
                tries += 1
        
        marks += get_marks(tries=tries, type="multichoice")
        print("Correct! Crescendo in music means to play gradually louder, the speed remains the same and is commonly seen in music sheets as the notation “<”")

        print("Which of these represent mezzo-forte? (Choose from a, b, c or d)")
        print("a) mp\nb) mf\nc) pp\nd) ff")
        answer = input("Your answer: ")
        tries += 1

        while answer != "b":
            if tries == 1:
                print("The first letters of the 2 words are the acronyms.")
                answer = input("Your answer: ")
                tries += 1
            else:
                answer = input("Incorrect! Re-enter your answer: ")
                tries += 1
        
        marks += get_marks(tries=tries, type="multichoice")
        print("Correct! The mezzo-forte, is put as “mf” in music sheets and means to play it moderately loud.")

    return marks

def init():
    selection = input("Choose a topic: dynamics, speed and tempo, beats or time signature and clef\nYour selection: ")
    marks = run_questions(selection)

    run_next = input("Would you like to do another topic? (y/n)\n")
    if run_next == "y" or run_next == "yes":
        topic = init()
        marks = run_questions(topic["questions"])
    else: 
        print(f"Cancelled topic selection. Thanks for playing! You earned a total of {marks} marks.")

init()