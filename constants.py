questions: object = {
    "dynamics": {
        "questions": [
            {
                "question": "What does a crescendo mean?",
                "options": [
                    {
                        "id": "a",
                        "answer": "Getting louder"
                    },
                    {
                        "id": "b",
                        "answer": "Getting quieter"
                    },
                    {
                        "id": "c",
                        "answer": "Getting faster"
                    },
                    {
                        "id": "d",
                        "answer": "Getting slower"
                    }
                ],
                "answer": "a",
                "hint": "It is similar to the english definition.",
                "message": "Crescendo in music means to play gradually louder, the speed remains the same and is commonly seen in music sheets as the notation “<”",
                "type": "multichoice"
            },
            {
                "question": "Which of these represent mezzo-forte?",
                "options": [
                    {
                        "id": "a",
                        "answer": "mp"
                    },
                    {
                        "id": "b",
                        "answer": "mf"
                    },
                    {
                        "id": "c",
                        "answer": "pp"
                    },
                    {
                        "id": "d",
                        "answer": "ff"
                    }
                ],
                "answer": "b",
                "hint": "The first letters of the 2 words are the acronyms",
                "message": "The mezzo-forte, is put as “mf” in music sheets and means to play it moderately loud.",
                "type": "multichoice"
            },
            {
                "question": "Forte is louder than mezzo-forte - true or false?",
                "options": [
                    {
                        "id": "a",
                        "answer": "true"
                    },
                    {
                        "id": "b",
                        "answer": "false"
                    }
                ],
                "answer": "a",
                "hint": "Mezzo means moderately",
                "message": "Mezzo-forte is moderately loud, forte is just loud.",
                "type": "true/false"
            }
        ]
    },
    "speed_tempo": {
        "questions": []
    },
    "beats": {
        "questions": []
    },
    "timesigs_clefs": {
        "questions": []
    }
}
"""
Object containing quiz questions for each topic.
"""

topics = {
    "dynamics": "dynamics",
    "speed and tempo": "speed_tempo",
    "beats": "beats",
    "time signature and Clef": "timesigs_clefs"
}
"""
Topics dictionary mapping more readable topic names into the questions dictionary keys.
"""

topic_list = [
    "dynamics",
    "speed and tempo",
    "beats",
    "time signature and clef"
]
"""
List of topics for the user to choose from.
"""
