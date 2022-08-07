#!/usr/bin/env python3

from typing import Any

questions: dict[str, Any] = {
    "dynamics": {
        "questions": [
            {
                "question": "What does a crescendo mean? (Choose from a, b, c or d)",
                "option_string": "a) Getting louder\nb) Getting quiter\nc) Getting faster\nd) Getting slower",
                "options": ["a", "b", "c", "d"],
                "answer": "a",
                "hint": "It is similar to the english definition.",
                "message": "Crescendo in music means to play gradually louder, the speed remains the same and is commonly seen in music sheets as the notation “<”",
                "type": "multichoice"
            },
            {
                "question": "Which of these represent mezzo-forte? (Choose from a, b, c or d)",
                "option_string": "a) mp\nb) mf\nc) pp\nd) ff",
                "options": ["a", "b", "c", "d"],
                "answer": "b",
                "hint": "The first letters of the 2 words are the acronyms.",
                "message": "The mezzo-forte, is put as “mf” in music sheets and means to play it moderately loud.",
                "type": "multichoice"
            },
            {
                "question": "Forte is louder than mezzo-forte - true or false? (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "a",
                "hint": "Mezzo means moderately.",
                "message": "Mezzo-forte is moderately loud, forte is just loud.",
                "type": "true/false"
            },
            {
                "question": "Mf and mp are equally loud - true or false? (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "b",
                "hint": "Mp means mezzo piano and mf means mezzo forte.",
                "message": "No notation in music have the same degree of loudness.",
                "type": "true/false"
            },
            {
                "question": "Rank these from quietest to loudest: (in the format 1, 2, 3, 4)",
                "option_string": "1) f\n2) mp\n3) ppp\n4) pp",
                "answer": ["3", "4", "2", "1"],
                "hint": "ppp just means it is more quieter than pp which is more quieter than p.",
                "message": "ppp means pianississimo, pp means pianissimo, mp means mezzo-piano, f means fort.",
                "type": "order"
            }
        ]
    },
    "speed_tempo": {
        "questions": [
            {
                "question": "Allegro is fast - true or false? (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "a",
                "hint": "It has the similar meaning to the english meaning of moving briskly fast.",
                "message": "Allegro is commonly referred to as the basis of the fast tempo",
                "type": "true/false"
            },
            {
                "question": "What does decelerando mean? (Choose from a, b, c, or d)",
                "option_string": "a) Getting faster\nb) Remain the same\nc) Getting slower\nd) Getting faster and then slower",
                "options": ["a", "b", "c", "d"],
                "answer": "c",
                "hint": "Decelerando has a the opposite meaning to acceleration.",
                "message": "Decelerando means to gradually play slower.",
                "type": "multichoice"
            },
            {
                "question": "Ritardando written on a music sheet is: (Choose from a, b, c, or d)",
                "option_string": "a) rit.\nb) r.\nc) rdd. \nd) rt.",
                "options": ["a", "b", "c", "d"],
                "answer": "a",
                "hint": "In music sheets, most of the time the words are shortened with the first letter(s).",
                "message": "Ritardando shortened is rit., this means to gradually slow down in the given area until it has reached the a tempo message.",
                "type": "multichoice"
            },
            {
                "question": "Rank these from the slowest to fastest: (in the format 1, 2, 3, 4)",
                "option_string": "1) Presto\n2) Lento\n3) Allegro\n4) Moderato",
                "answer": ["2", "4", "3", "1"],
                "hint": "Presto is the fastest.",
                "message": "Lento is slow, moderato is middle speed, allegro is fast, presto is extremely fast.",
                "type": "order"
            },
            {
                "question": "What is name of the musical device that helps you keep in tempo? (Word answer)",
                "answer": "metronome",
                "hint": "Begins with the letter M and makes clicking sounds on each beat",
                "message": "The metronome is important for all levels of musicians because it keeps a consistent tempo which helps reduce the effects of musicians constantly speeding up or slowing down in certain parts.",
                "type": "word"
            }
        ]
    },
    "beats": {
        "questions": [
            {
                "question": "How many beats does a quaver have? (Choose from a, b, c, or d)",
                "option_string": "a) 1 beat\nb) 1/2 beat\nc) 1/4 beat\nd)1/8 beat",
                "options": ["a", "b", "c", "d"],
                "answer": "b",
                "hint": "It is shorter than 1 beat.",
                "message": "A quaver is shown as a crotchet with 1 singular tail indicating it is halved once, same thing for ones that have more tails.",
                "type": "multichoice"
            },
            {
                "question": "Which of the following lasts 4 beats? (Choose from a, b, c, or d)",
                "option_string": "a) Crotchet\nb) Minim\nc) Dotted-minim\nd) Semi-breve",
                "options": ["a", "b", "c", "d"],
                "answer": "d",
                "hint": "It is not a minim.",
                "message": "A crotchet is 1 beat, a minim is 2 beats, a dotted-minim 3 beats and a semi-breve is 4 beats.",
                "type": "multichoice"
            },
            {
                "question": "How many beats is the following bar: Crotchet + Quaver + Crotchet + Semi-quaver (Choose from a, b, c, or d)",
                "option_string": "a) 2 beats\nb) 2.75 beats\nc) 4 beats\nd) 3.75 beats",
                "options": ["a", "b", "c", "d"],
                "answer": "b",
                "hint": "A semi-quaver is ¼ of a beat.",
                "message": "1 + ½ + 1 + ¼ = 2.75",
                "type": "multichoice"
            },
            {
                "question": "Rank these from the shortest to the longest beats: (in the format 1, 2, 3, 4)",
                "option_string": "1) Minim\n2) Semi-quaver\n3) Quaver\n4) Crotchet",
                "answer": ["2", "3", "4", "1"],
                "hint": "A quaver is shown as a crotchet with 1 singular tail indicating it is halved once, a semi-quaver has 2 tails, a demi-semi-quaver has 3 tails.",
                "message": "A semi-quaver is ¼ of a beat, quaver is ½ of a beat, crotchet is 1 beat and minim is 2 beats.",
                "type": "order"
            },
            {
                "question": "True or false, a dotted crotchet is ⅓ of a beat: (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "b",
                "hint": "For example, a dotted crotchet is 1.5 of a beat.",
                "message": "The dotted in front of the beat is the original beat (without the dotted) halved, then using the result that was halved to add to the original.",
                "type": "true/false"
            }
        ]
    },
    "timesigs_clefs": {
        "questions": [
                        {
                "question": "The treble clef represents only the right side of the piano from the middle C: (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "b",
                "hint": "Both right hands and left hands can use the treble clef.",
                "message": "The notes on a treble clef sheet can go below the middle C, it can in fact go to as low as you want with the right notations.",
                "type": "true/false"
            },
            {
                "question": "When a music sheet says “4/4” in the beginning of the piece, what does it mean? (Choose from a, b, c, or d)",
                "option_string": "a) There are 1 beat in each bar\nb) There are 4 beats in each bar\nc) There are 8 beats in each bar\nd) There are 16 beats in each bar",
                "options": ["a", "b", "c", "d"],
                "answer": "b",
                "hint": "The 4 in the denominator means you need to read the bar as each beat being ¼ of it, total is 4.",
                "message": "When the 4 is in the denominator, it means that you need to read the bar as each beat being ¼ of the 4 in total, therefore, since there is 4 in the numerator, it means that there is 4 beats in each bar.",
                "type": "multichoice"
            },
            {
                "question": "When a music sheet says “3/8” in the beginning of the piece, what does it mean? (Choose from a, b, c, or d)",
                "option_string": "a) There are ⅜ beats in each bar\nb) There are 1 beat in each bar\nc) There are 1.5 beats in each bar\nd) There are 2 beats in each bar",
                "options": ["a", "b", "c", "d"],
                "answer": "c",
                "hint": "The 8 in the denominator means that from the total of 4, ⅛ or 4 which is 0.5 beats.",
                "message": "The 8 in the denominator means that from the total of 4, ⅛ or 4 which is 0.5 beats, since there is 3 in the numerator, there is 3 of the 0.5 beats making 1.5 in each bar.",
                "type": "multichoice"
            },
            {
                "question": "Rank these with the smallest total beats in each bar to the largest in total beats in each bar: (in the format 1, 2, 3, 4)",
                "option_string": "1) 2/8\n2) 2/2\n3) 2/2\n4) 3/8",
                "answer": ["1", "4", "3", "2"],
                "hint": "Same rule as from previous question.", 
                "message": "2/8 is 1 beat, ⅜ is 1.5 beats, 2/4 is 2 beats, 2/2 is 4 beats.",
                "type": "order"
            },
            {
                "question": "Can the time signature in a piece change midway of a piece/song? (Choose from a or b)",
                "option_string": "a) true\nb) false",
                "options": ["a", "b"],
                "answer": "a",
                "hint": "Music is flexible and is what gives it the complexity and range.",
                "message": "The time signature can change at any point in the piece, it can change 1 bar after the next, it can also change how many times it wants.",
                "type": "true/false"
            }
        ]
    }
}
"""
Object containing quiz questions for each topic.
"""

topics: dict[str, str] = {
    "dynamics": "dynamics",
    "speed and tempo": "speed_tempo",
    "beats": "beats",
    "time signature and clef": "timesigs_clefs"
}
"""
Topics dictionary mapping more readable topic names into the questions dictionary keys.
"""

topic_list: list[str] = [
    "dynamics",
    "speed and tempo",
    "beats",
    "time signature and clef",
    "all"
]
"""
List of topics for the user to choose from.
"""
