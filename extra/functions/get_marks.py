def get_marks(tries: int = 0, type: str = "", correct_places: int = 0) -> int:
    """
    Calculates the number of marks received for a question.
    """
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