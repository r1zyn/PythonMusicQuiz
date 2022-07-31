from functions.choose_topic import choose_topic
from functions.run_topic import run_topic

marks: int = 0
topic: dict = choose_topic()

marks += run_topic(topic, marks)