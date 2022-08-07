from time import sleep # Import sleep function to create delays between each question
from typing import Any, Union # Import Union type to support union types, Any to support any type
from constants import questions, topics, topic_list # Importt constants
from re import search, Match # Import regex search function and Match type

# Function to return the number of marks earned from a question
def get_marks(tries: int = 0, type: str = "", correct_places: int = 0) -> int: 
    """
    Calculates the number of marks received for a question.
    """

    if type.lower() == "multichoice" or type.lower() == "word": # If the question type is a multiple choice or word question
        if tries == 1:
            return 10 # If the user gets the question right on the first try, return 10 marks
        elif tries == 2:
            return 5 # If the user gets the question right on the second try, return 5 marks
        elif tries == 3:
            return 3 # If the user gets the question right on the third try, return 3 marks
        elif tries == 4:
            return 1 # If the user gets the question right on the fourth try, return 1 mark
        else: 
            return 0 # Otherwise, return 0 marks
    elif type.lower() == "true/false": # If the question type is a true/false question
        if tries == 1:
            return 10 # If the user gets the question right on the first try, return 10 marks
        elif tries == 2:
            return 1 # If the user gets the question right on the second try, return 1 mark
        else:
            return 0
    elif type.lower() == "order": # If the question type is an order question
        if correct_places == 4:
            return 10 # If the user gets 4 places correct, return 10 marks
        elif correct_places == 3:
            return 5 # If the user gets 3 places correct, return 5 marks
        elif correct_places == 2:
            return 3 # If the user gets 2 places correct, return 3 marks
        elif correct_places == 1:
            return 1 # If the user gets 1 place correct, return 1 mark
        else: 
            return 0 # Otherwise, return 0 marks

# Function to run the questions in a provided question list
def run_questions(question_list: dict[str, Any]) -> int: 
    """
    Runs the questions from the question list from the topic the user selected.
    """

    marks: int = 0 # Total number of marks earned from the list
    tries: int = 0 # Number of tries for a question

    for question in question_list: # Iterate through each question dict in the question list
        print("Question: " + question["question"]) # Prints the question

        if question["type"] == "order": # If the question type is an order question
            print("Options:\n" + question["option_string"]) # Prints the options
            print("Hint: " + question["hint"]) # Prints the hint for the question

            answer: str = input("Enter your answer: ").lower() # The user's input
            correct_places: int = 0 # Number of correct places the user gets in the ordering right
            option_amount: int = len(question["answer"]) # The number of options available for ordering
            matches: Union[Match[str], None] = search("^(\d\,\s){3}\d$", answer) # Regex matches to ensure their answer is propery formatted

            # Regex breakdown for: ^(\d\,\s){3}\d$
            # ^ Represents the start of the searching string
            # (\d\,\s) is a group where \d represents any digit, \, represents a command and \s represents a whitespace character
            # {3} means to search for 3 of the group
            # \d represents a single digit after the replicated group
            # $ represents the end of the searching string

            while matches == None: # Check if no matches in the answer for the required format is found
                answer: str = input("Invalid format, please try again: ").lower() # While the user's answer is in an invalid format, prompt them to re-enter it

            while not all(item in answer.split(", ") for item in question["answer"]): # Compares the values in the answer list to the user's answer
                answer: str = input("Invalid answer, please try again: ").lower() # While the user's does not include the values in the answer, prompt them to re-enter it

            for i in range(option_amount): # Iterate through each value in the answer
                if answer.split(", ")[i] == question["answer"][i]: # Checks if the value is in the correct place
                    correct_places += 1 # Increase the number of correct places by 1

            earned_marks: int = get_marks(type=question["type"], correct_places=correct_places) # Returns the number of marks based on the correct places (for ordering question)
            marks += earned_marks # Append the new marks to the existing total of marks
            print("You completed the question with " + str(correct_places) + " correct places. " + question["message"]) # Prints the number of correct places the user got and the message for the question 
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks from the topic.") # Prints the number of marks the user earned and the total number of marks
        elif question["type"] == "word": # If the question type is a word question
            answer: str = input("Enter your answer: ").lower() # The user's input

            tries += 1 # Increase the number of tries by 1

            while answer != question["answer"].lower(): # While the user's answer is not the correct answer
                if tries == 1: # If the user is on their first try
                    print("Hint: " + question["hint"]) # Print the hint for the question
                    answer: str = input("Enter your answer: ").lower() # Recollect their answer
                else:
                    answer: str = input("Incorrect! Re-enter your answer: ").lower() # Otherwise, ask for another answer

                tries += 1 # Each time the answer is incorrect, increase the number of tries by 1

            earned_marks: int = get_marks(tries=tries, type=question["type"]) # Returns the number of marks based on the number of tries
            marks += earned_marks # Append the new marks to the existing total of marks
            print("Correct! " + question["message"]) # Prints the message for the question
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks from the topic.") # Prints the number of marks the user earned and the total number of marks
        else: # If the question type is a multiple choice or true/false question
            print("Options:\n" + question["option_string"]) # Prints the options
            answer: str = input("Enter your answer: ").lower() # The user's input

            while not answer in question["options"]: # While the user's answer is not one of the options
                answer: str = input("Invalid answer, please try again: ").lower() # Prompt them to re-enter their answer

            tries += 1 # Increase the number of tries by 1

            while answer != question["answer"].lower(): # While the user's answer is not the correct answer
                if tries == 1: # If the user is on their first try
                    print("Hint: " + question["hint"]) # Print the hint for the question
                    answer: str = input("Enter your answer: ").lower() # Recollect their answer
                else: 
                    answer: str = input("Incorrect! Re-enter your answer: ").lower() # Otherwise, ask for another answer

                tries += 1 # Each time the answer is incorrect, increase the number of tries by 1

            earned_marks: int = get_marks(tries=tries, type=question["type"]) # Returns the number of marks based on the number of tries
            marks += earned_marks # Append the new marks to the existing total of marks
            print("Correct! " + question["message"]) # Prints the message for the question
            print(f"You earned a total of {earned_marks} marks. You now have {marks} marks from the topic.") # Prints the number of marks the user earned and the total number of marks

        tries: int = 0  # Reset the number of tries for the next question
        sleep(2) # Pause the program for 2 seconds

    return marks # Return the total number of marks the user earned

def run_selection() -> None:
    """
    Initiates the quiz by asking a user to input a quiz topic, then runs the question for the given topic.
    Gives the user to continue with other topics once they have completed a topic.
    """

    selection: str = input("Choose a topic: dynamics, speed and tempo, beats, time signature and clef or all\nYour selection: ").lower() # The user's topic selection

    while not selection in topic_list: # Checks if the user's selection is valid
        selection = input("Please choose a valid topic: dynamics, speed and tempo, beats, time signature and clef or all\nYour selection: ").lower() # Prompt them to re-enter their answer

    marks: int = 0 # Initiate marks variable

    if selection == "all": # Checks if the user wants to run all topics
        for topic in questions.values(): # Iterates through each topic
            marks += run_questions(topic["questions"]) # Runs the questions in each topic and append the number of received marks to the marks variable

        print(f"Thanks for playing! You earned a total of {marks} marks.") # Prints a message thanking the user for playing, and displays the total number of marks they earned
    else:
        topic: str = questions[topics[selection]] # Gets the topic 
        marks: int = run_questions(topic["questions"]) # Otherwise, runs the questions for the selected topic and appends the number of received marks to the marks variable
        print(f"Thanks for playing! You earned a total of {marks} marks.") # Prints a message thanking the user for playing, and displays the total number of marks they earned

    run_next: str = input(f"Would you like to do another topic? (y/n)\n").lower() # Asks the user if they want to continue
    if run_next == "y" or run_next == "yes":
        run_selection() # If they choose yes, run the selection process again
    else: 
        exit(0) # Otherwise, exit the program with code 0 (success code)

def init() -> None:
    """
    Function to initialise the program - introduces the quiz and explains how it works, then runs the actual quiz itself.
    """

    print("-----------[ Python Music Quiz ]-----------")
    print("Welcome to the Python music quiz! This is a music quiz written in Python to help you user prepare for music theories ranging from 4 different topics:") # Introduces the quiz
    print(" » Dynamics\n » Speed and tempo\n » Beats\n » Time signature and clef\n") # Displays the available quiz topics
    print("You will receive a variety of type of questions in each topic: ") # Talks about the types of questions and the available marks for each type 
    print(" » Multiple choice questions\n   1st try: 10 marks\n   2nd try: 5 marks\n   3rd try: 3 marks\n   4th try: 1 mark\n")
    print(" » Word questions\n   1st try: 10 marks\n   2nd try: 5 marks\n   3rd try: 3 marks\n   4th try: 1 mark\n")
    print(" » True/False questions\n   1st try: 10 marks\n   2nd try: 1 mark\n")
    print(" » Order questions\n   4 correct places: 10 marks\n   3 correct places: 5 marks\n   2 correct places: 3 marks\n   1 correct place: 1 mark\n")
    print("You will receive one hint after your first try for every question.") # Talks about hints
    print("Note: there will be 2 second delay after every question.") # Notifies user 2 second delays will occur, as user may be think there is an issue with the program when it unexpected pauses for 2 seconds

    run_selection() # Begins the actual quiz 

init() # Runs the program