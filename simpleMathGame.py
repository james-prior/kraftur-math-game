#!/usr/bin/env python3.6

# Math problems add and subtraction v 1.0

import sys
from random import choices
from functools import partial

total_n_correct = 0
total_n_wrong = 0
total_n_extra_points = 0

prompt = '''

For "Addition" type:     add 

For "Subtraction" type:  subtract. 

To see your statistics type: stats 

To quit type:            quit 
'''


def game(prompt):
    actions = {
        'add': addition,
        'subtract': subtraction,
        'stats': show_statistics,
        'quit': exit_,
    }

    for choice in iter(partial(input, prompt), ''):
        try:
            action = actions[choice]
        except KeyError:
            print('Please type "add" or "subtract" or "stats" ')  # what about quit?
        else:
            action()


def exit_():
    prompt = 'Are you sure you want to quit? Y/n '
    for choice in iter(partial(input, prompt), ''):
        choice = choice.lower().strip()
        if choice == 'y':
            sys.exit()
        elif choice == 'n':
            return

        print('Please enter "Y" or "n" ')


def show_statistics():
    percentage_correct = 100 * (
        total_n_correct / (total_n_correct + total_n_wrong))
    print('Total Correct:      ', total_n_correct)
    print('Total Wrong:        ', total_n_wrong)
    print('Total Extra Points: ', total_n_extra_points)
    print('Percentage Correct: ', percentage_correct)


def get_truth_of_answer(problem, correct_answer):
    answer = input(problem + ' ')
    return answer == correct_answer


def do_problems(action_name, n, problems_and_answers):
    global total_n_correct
    global total_n_wrong
    global total_n_extra_points

    n_correct = 0
    n_wrong = 0
    n_extra_points = 0
    print('You chose %s! ' % action_name)
    for problem, answer in choices(problems_and_answers, k=n):
        if get_truth_of_answer(problem, answer):
            total_n_correct += 1
            total_n_extra_points += 1
            n_correct += 1
            n_extra_points += 1
            print('[+] Correct! + 1xp')
        else:
            print('[-] Wrong! ')
            total_n_wrong += 1
            n_wrong += 1
    print()
    print('Number Wrong:        ', n_wrong)
    print('Number Correct:      ', n_correct)
    print('Extra Points Gained: ', n_extra_points)

def addition():
    do_problems('Addition', 10, addition_problems_and_answers)

def subtraction():
    do_problems('Subtraction', 10, subtraction_problems_and_answers)

def munge(problems_and_answers_text):
    return [
        tuple(term.strip() for term in line.split(','))
        for line in problems_and_answers_text.split('\n')
        if line.strip()
    ]

addition_problems_and_answers_text = '''
    11 + 11, 22
    11 + 2, 13
    11 + 3, 14
    11 + 4, 15
    11 + 5, 16
    11 + 6, 17
    11 + 7, 18
    11 + 8, 19
    11 + 9, 20
    12 + 2, 14
    12 + 3, 15
    12 + 4, 16
    12 + 5, 17
    12 + 6, 18
    12 + 7, 19
    12 + 8, 20
    12 + 9, 21
    3 + 3, 6
    3 + 4, 7
    3 + 5, 8
    3 + 6, 9
    3 + 7, 10
    3 + 8, 11
    3 + 9, 12
    4 + 4, 8
    4 + 5, 9
    4 + 6, 10
    4 + 7, 11
    4 + 8, 12
    4 + 9, 13
    5 + 5, 10
    5 + 6, 11
    5 + 8, 13
    5 + 9, 14
    6 + 6, 12
    6 + 7, 13
    6 + 8, 14
    6 + 9, 15
    7 + 7, 14
    7 + 8, 15
    7 + 9, 16
    8 + 8, 16
    8 + 9, 17
    9 + 9, 18
    10 + 4, 14
    10 + 5, 15
    10 + 6, 16
    10 + 7, 17
    10 + 8, 18
    10 + 9, 19
    10 + 10, 20
    13 + 3, 16
    13 + 4, 17
    13 + 5, 18
    13 + 6, 19
    13 + 7, 20
    13 + 8, 21
    13 + 9, 22
    13 + 10, 23
    13 + 11, 24
    13 + 12, 25
    13 + 13, 26
'''
addition_problems_and_answers = munge(addition_problems_and_answers_text)

subtraction_problems_and_answers_text = '''
    9 - 1, 8
    9 - 2, 7
    9 - 3, 6
    9 - 4, 5
    9 - 5, 4 9 - 6, 3
    9 - 7, 2
    9 - 8, 1
    9 - 9, 0
    8 - 1, 7
    8 - 2, 6
    8 - 3, 5
    8 - 4, 4
    8 - 5, 3
    8 - 6, 2
    8 - 7, 1
    8 - 8, 0
    17 - 1, 16
    17 - 2, 15
    17 - 3, 14
    17 - 4, 13
    17 - 5, 12
    17 - 6, 11
    17 - 7, 10
    16 - 1, 15
    16 - 2, 14
    16 - 3, 13
    16 - 4, 12
    16 - 5, 11
    16 - 6, 10
    5 - 1, 4
    5 - 2, 3
    5 - 3, 2
    5 - 4, 1
    5 - 5, 0
    4 - 1, 3
    4 - 2, 2
    4 - 3, 1
    4 - 4, 0
    3 - 1, 2
    3 - 2, 1
    3 - 3, 0
    12 - 10, 2
    12 - 2, 10
    12 - 11, 1
    12 - 9, 3
    12 - 8, 4
    12 - 7, 5
    12 - 6, 6
    12 - 5, 7
    12 - 4, 8
    12 - 3, 9
    12 - 2, 10
    12 - 1, 11
'''
subtraction_problems_and_answers = munge(subtraction_problems_and_answers_text)


def main():
    name = input('What is your name? ')
    print('Hello ' + name + '! Welcome to Math Adventure!')
    game(prompt)

if __name__ == '__main__':
    main()
