question_prompt = [
    'what is my name\n (a)Ahmad\n (b)Ali\n (c)Aslam\n (d)Amjad\n',
    'where do I study\n(a)MIT\n (b)HARVARD\n (c)Oxford\n (d)LUMS\n',
    'How much I earn\n(a)5000$\n(b)700$\n(c)6000$\n(d)20000$\n'
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompt[0] , 'a'),
    Question(question_prompt[1], 'b'),
    Question(question_prompt[2] , 'd'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')

run_test(questions)
