from functions.get_marks import get_marks
import re

def format_option(option: str) -> str:
    """
    Formats options into a string.
    """
    return option["id"] + ") " + option["answer"]

def run_question(question) -> int:
    """
    Initiates a question for the user.
    """
    tries: int = 0
    options: list[str] = []
    marks: int = 0

    print("Question: " + question["question"])

    if question["type"] == "multichoice" or question["type"] == "true/false":
        print("Options:\n" + "\n".join(map(format_option, question["options"])))
        
        for option in question["options"]:
            options.append(option["id"])

        answer: str = input("Enter your answer: ").lower()

        while not answer in options:
            answer: str = input("Please provide a valid answer: ").lower()

        tries += 1

        while answer != question["answer"]:
            if tries == 1:
                print("Here's a hint: " + question["hint"])
                answer: str = input("Enter your answer: ").lower()
            else:
                answer: str = input("Incorrect! Try again: ").lower()

            while not answer in options:
                answer: str = input("Please provide a valid answer: ").lower()
            
            tries += 1

        marks: int = get_marks(tries, question["type"])
    elif question["type"] == "word":
        answer: str = input("Enter your answer: ").lower()

        while answer.lower() != question["answer"].lower():
            if tries == 1:
                print("Here's a hint: " + question["hint"])
                answer: str = input("Enter your answer: ").lower()
            else:
                answer: str = input("Incorrect! Try again: ").lower()

            tries += 1

        marks: int = get_marks(tries, question["type"])
    elif question["type"] == "order":
        print("Options:\n" + "\n".join(map(format_option, question["options"])))
        
        answer: str = input("Enter your answer: ").lower()
        correct_places: int = 0
        matches: re.Match = re.search("^(\d\,\s)+\d$", answer)

        while not matches:
            answer: str = input("Please provide a valid answer: ").lower()

        answer: list[str] = answer.split(", ")

        for i, v in enumerate(answer):
            if v == question["answer"][i]:
                correct_places += 1

        marks: int = get_marks(type="order", correct_places=correct_places)
               
    if question["type"] == "order":
        print("You got " + str(correct_places) + " correct place(s)!" + " You earned " + str(marks) + " marks.")
    else:
        print("Correct! " + question["message"] + " You earned " + str(marks) + " marks with " + str(tries) + " tries.")
        
    return marks
    