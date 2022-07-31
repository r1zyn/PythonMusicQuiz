def get_marks(tries: int, type: str) -> int:
    """
    Calculates the number of marks received for a question.
    """
    if type.lower() == "multichoice" or type.lower() == "word" or type.lower() == "order":
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