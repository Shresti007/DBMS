from junk1 import Question


question_prompts = [
    " What colors are apples?\n (a) red/green\n(b)purple\n(c)yellow\n\n"
    "what color are bananas?\n (a) Yellow/Green\n(b) red\n (c) orange\n\n"
    "what color are straberies?\n (a)yellow\n(b) red\n(c) green\n\n"
]

questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),

]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print("You got" + str(score)+ "/" + str(len(questions)) + "correct")

run_test(questions)