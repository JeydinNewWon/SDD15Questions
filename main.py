from question import Question
from choice import Choice

def print_ascii(file):
    with open(file) as f:
        print(f.read())
        f.close()

questions_and_answers = open('questions_and_answers.txt', 'r')

question_list = []

for line in questions_and_answers:
    question_data = line.strip().split(';')

    question = question_data[0]

    a = question_data[1]
    b = question_data[2]
    c = question_data[3]
    d = question_data[4]

    answer = question_data[5]

    question_list.append(Question(question, Choice(a, b, c, d), answer))

questions_and_answers.close()
print_ascii('welcome.txt')

number_of_correct = 0

for question in question_list:
    print(question.question + '\n')
    choices = question.choices
    print("(A) " + choices.a)
    print("(B) " + choices.b)
    print("(C) " + choices.c)
    print("(D) " + choices.d + "\n")

    answer = input("Your Answer: ")

    if answer is None:
        break

    formatted_answer = answer.lower()

    if formatted_answer == question.answer:
        print('\nCorrect!')
        number_of_correct += 1
    else:
        print('Incorrect. The answer was {}.'.format(question.answer.upper()))

    print('-' * 100)
    print('\n')

print_ascii('finish.txt')

print('\nYou got {}/15 correct.'.format(number_of_correct))