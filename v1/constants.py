questions: object = {
    "dynamics": {
        "questions": [
            {
                "question": "What does a crescendo mean? (Choose from a, b, c or d)",
                "options": "a) Getting louder\nb) Getting quiter\nc) Getting faster\nd) Getting slower",
                "answer": "a",
                "hint": "It is similar to the english definition.",
                "message": "Crescendo in music means to play gradually louder, the speed remains the same and is commonly seen in music sheets as the notation “<”",
                "type": "multichoice"
            },
            {
                "question": "Which of these represent mezzo-forte? (Choose from a, b, c or d)",
                "options": "a) mp\nb( mf\nc) pp\nd) ff",
                "answer": "b",
                "hint": "The first letters of the 2 words are the acronyms.",
                "message": "The mezzo-forte, is put as “mf” in music sheets and means to play it moderately loud.",
                "type": "multichoice"
            },
            {
                "question": "Forte is louder than mezzo-forte - true or false? (Choose from a or b)",
                "options": "a) true\nb) false",
                "answer": "a",
                "hint": "Mezzo means moderately.",
                "message": "Mezzo-forte is moderately loud, forte is just loud.",
                "type": "true/false"
            },
            {
                "question": "Mf and mp are equally loud - true or false? (Choose from a or b)",
                "options": "a) true\nb) false",
                "answer": "b",
                "hint": "Mp means mezzo piano and mf means mezzo forte.",
                "message": "No notation in music have the same degree of loudness.",
                "type": "true/false"
            },
            {
                "question": "Rank these from quietest to loudest: (in the format 1, 2, 3, 4)",
                "options": "1) f\n2) mp\n3) ppp\n4) pp",
                "answer": ["3", "4", "2", "1"],
                "hint": "ppp just means it is more quieter than pp which is more quieter than p.",
                "message": "ppp means pianississimo, pp means pianissimo, mp means mezzo-piano, f means fort",
                "type": "order"
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
    "time signature and clef": "timesigs_clefs"
}
"""
Topics dictionary mapping more readable topic names into the questions dictionary keys.
"""