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
                "hint": "The first letters of the 2 words are the acronyms.",
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
                "hint": "Mezzo means moderately.",
                "message": "Mezzo-forte is moderately loud, forte is just loud.",
                "type": "true/false"
            },
            {
                "question": "Mf and mp are equally loud - true or false?",
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
                "answer": "b",
                "hint": "Mp means mezzo piano and mf means mezzo forte.",
                "message": "No notation in music have the same degree of loudness.",
                "type": "true/false"
            },
            {
                "question": "Rank these from quietest to loudest: (in the format 1, 2, 3, 4)",
                "options": [
                    {
                        "id": "1",
                        "answer": "f"
                    },
                    {
                        "id": "2",
                        "answer": "mp"
                    },
                    {
                        "id": "3",
                        "answer": "ppp"
                    },
                    {
                        "id": "4",
                        "answer": "pp"
                    }
                ],
                "answer": ["3", "4", "2", "1"],
                "hint": "ppp just means it is more quieter than pp which is more quieter than p.",
                "message": "ppp means pianississimo, pp means pianissimo, mp means mezzo-piano, f means fort",
                "type": "order"
            }
        ]
    },
    "speed_tempo": {
        "questions": [
            {
                "question": "Allegro is fast - true or false?",
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
                "hint": "Similar meaning to the english meaning of moving briskly fast.",
                "message": "Allegro is commonly referred to as the basis of the fast tempo.",
                "type": "true/false"
            },
            {
                "question": "What does decelerando mean?",
                "options": [
                    {
                        "id": "a",
                        "answer": "Getting faster"
                    },
                    {
                        "id": "b",
                        "answer": "Remain the same"
                    },
                    {
                        "id": "c",
                        "answer": "Getting slower"
                    },
                    {
                        "id": "d",
                        "answer": "Getting faster then slower"
                    }
                ],
                "answer": "c",
                "hint": "Decelerando has a similar meaning to decceleration.",
                "message": "Decelerando means to gradually play slower.",
                "type": "multichoice"
            },
            {
                "question": "Ritardando written on a music sheet is:",
                "options": [
                    {
                        "id": "a",
                        "answer": "rit."
                    },
                    {
                        "id": "b",
                        "answer": "r."
                    },
                    {
                        "id": "c",
                        "answer": "rdd."
                    },
                    {
                        "id": "d",
                        "answer": "rt."
                    }
                ],
                "answer": "a",
                "hint": "DIn music sheets, most of the time the words are shortened with the first letter(s).",
                "message": "Ritardando shortened is rit., this means to gradually slow down in the given area until it has reached the “a tempo” message”.",
                "type": "multichoice"
            },
            {
                "question": "What is the name of the musical device that helps you keep in tempo?",
                "answer": "metronome",
                "hint": "Begins with the letter M and makes clicking sounds on each beat.",
                "message": "The metronome is important for all levels of musicians because it keeps a consistent tempo which helps reduce the effects of musicians constantly speeding up or slowing down in certain parts.",
                "type": "word"
            }
        ]
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
