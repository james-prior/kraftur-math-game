#!/usr/bin/env python3.6

"""
Practices addition and subtraction math problems.
v 1.0
"""

import sys
from random import choices
from functools import partial, reduce
from operator import add, sub

total_n_correct = 0
total_n_wrong = 0
total_n_extra_points = 0

prompt = '''

For "Addition" type:     add 

For "Subtraction" type:  subtract. 

To see your statistics type: stats 

To quit type:            quit 
'''


def practice(prompt):
    actions = {
        'add': practice_addition,
        'subtract': practice_subtraction,
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
    percentage_correct = 100 * total_n_correct / (
        total_n_correct + total_n_wrong)
    print('Total Correct:     ', total_n_correct)
    print('Total Wrong:       ', total_n_wrong)
    print('Total Extra Points:', total_n_extra_points)
    print('Percentage Correct:', percentage_correct)


def get_truth_of_answer(operator, *operands):
    operator_symbol = {
        add: '+',
        sub: '-',
    }
    symbol = ' %s ' % operator_symbol[operator]
    problem = symbol.join(map(str, operands))
    correct_answer = str(reduce(operator, operands))
    answer = input(problem + ' ')
    return answer == correct_answer


def do_problems(action_name, n, operator, problems_and_answers):
    global total_n_correct
    global total_n_wrong
    global total_n_extra_points

    n_correct = 0
    n_wrong = 0
    n_extra_points = 0
    print('You chose %s!' % action_name)
    for operands in choices(problems_and_answers, k=n):
        if get_truth_of_answer(operator, *operands):
            total_n_correct += 1
            total_n_extra_points += 1
            n_correct += 1
            n_extra_points += 1
            print('[+] Correct! + 1 extra point')
        else:
            print('[-] Wrong! ')
            total_n_wrong += 1
            n_wrong += 1
    print()
    print('Number Wrong:       ', n_wrong)
    print('Number Correct:     ', n_correct)
    print('Extra Points Gained:', n_extra_points)

def practice_addition():
    do_problems('Addition', 10, *addition_problems)

def practice_subtraction():
    do_problems('Subtraction', 10, *subtraction_problems)

def munge(problems_text):
    return [
        tuple(int(operand.strip()) for operand in line.split())
        for line in problems_text.split('\n')
        if line.strip()
    ]

addition_problems_text = '''
    11 11
    11 11 11
    11 11 11 5
    1 2 3 4 5
    11 11
    11 2
    11 3
    11 4
    11 5
    11 6
    11 7
    11 8
    11 9
    12 2
    12 3
    12 4
    12 5
    12 6
    12 7
    12 8
    12 9
    3 3
    3 4
    3 5
    3 6
    3 7
    3 8
    3 9
    4 4
    4 5
    4 6
    4 7
    4 8
    4 9
    5 5
    5 6
    5 8
    5 9
    6 6
    6 7
    6 8
    6 9
    7 7
    7 8
    7 9
    8 8
    8 9
    9 9
    10 4
    10 5
    10 6
    10 7
    10 8
    10 9
    10 10
    13 3
    13 4
    13 5
    13 6
    13 7
    13 8
    13 9
    13 10
    13 11
    13 12
    13 13
'''
addition_problems = (
    add,
    munge(addition_problems_text)
)

subtraction_problems_text = '''
    9 1
    9 2
    9 3
    9 4
    9 5
    9 7
    9 8
    9 9
    8 1
    8 2
    8 3
    8 4
    8 5
    8 6
    8 7
    8 8
    17 1
    17 2
    17 3
    17 4
    17 5
    17 6
    17 7
    16 1
    16 2
    16 3
    16 4
    16 5
    16 6
    5 1
    5 2
    5 3
    5 4
    5 5
    4 1
    4 2
    4 3
    4 4
    3 1
    3 2
    3 3
    12 10
    12 2
    12 11
    12 9
    12 8
    12 7
    12 6
    12 5
    12 4
    12 3
    12 2
    12 1
'''
subtraction_problems = (
    sub,
    munge(subtraction_problems_text)
)


def main():
    name = input('What is your name? ')
    print('Hello ' + name + '! Welcome to Math Adventure!')
    practice(prompt)

if __name__ == '__main__':
    main()
