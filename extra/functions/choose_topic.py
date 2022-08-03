from extra.constants import questions, topics, topic_list

def choose_topic() -> list:
    """
    Initiates the program by asking a user to input a quiz topic, then returns the given topic.
    """

    chosen_topic: str = input(f"Choose a topic: {', '.join(topic_list)}\nYour topic: ").lower()
    while not chosen_topic in topic_list:
        chosen_topic: str = input(f"Please choose a valid topic: {', '.join(topic_list)}\nYour topic: ").lower()
    
    chosen_topic: list = questions[topics[chosen_topic]]
    return chosen_topic