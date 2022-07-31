from functions.get_marks import get_marks

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

    print("Question: " + question["question"])
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

    print("Correct! " + question["message"] + " You earned " + str(get_marks(tries, question["type"])) + " marks with " + str(tries) + " tries.")
    return get_marks(tries, question["type"])
    