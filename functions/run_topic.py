from functions.choose_topic import choose_topic
from functions.run_question import run_question

def run_topic(topic: object, marks: int) -> int:
    """
    Uses the given topic to select questions from the certain topic and begin asking the user the questions.
    """
    new_marks: int = 0
    questions: list = topic["questions"]

    for question in questions:
        new_marks += run_question(question)

    print(f"Congratulations on completing the topic! You earned {new_marks} marks.")
    run_next: str = input(f"Would you like to do another topic? (y/n)\n").lower()
    if run_next == "y" or run_next == "yes":
        topic = choose_topic()
        run_topic(topic, new_marks + marks)
    else: 
        print(f"Cancelled topic selection. Thanks for playing! You earned a total of {new_marks + marks} marks.")
    return new_marks