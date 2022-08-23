# Multiple choice quiz from freeCodeCamp

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Yellow\n(c) Magenta\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

question_answers = [
    "a",
    "b",
    "b"
]

questions = [
    Question(question_prompts[0], question_answers[0]),
    Question(question_prompts[1], question_answers[1]),
    Question(question_prompts[2], question_answers[2])
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return (f"You got {score}/{len(questions)} right")

run_test(questions)