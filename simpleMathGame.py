#!/usr/bin/env python3

# Math questions add and subtraction v 1.0

import random
import sys
from functools import partial

num_correct = 0
num_wrong = 0
xp_total = 0
name = input('What is your name? ')
print('Hello ' + name + '! Welcome to Math Adventure!')


prompt = '''

For "Addition" type:     add 
'
For "Subtraction" type:  subtract. 
'
For your xp totals type: xp 
'
To quit type:            quit 
'''


def game(prompt):
    actions = {
        'add': addition,
        'subtract': subtraction,
        'xp': xpPoints,
    }

    for choice in iter(partial(input, prompt), 'quit'):
        try:
            action = actions[choice]
        except KeyError:
            print('Please type "add" or "subtract" or "xp" ')  # what about quit?
        else:
            return action()
    else:
        exit_()


def exit_():
    userInput = input('Are you sure you want to quit? Y/n ')
    if userInput == ('Y') or userInput == ('y'):
        sys.exit()
    elif userInput == ('N') or userInput == ('n'):
        return game()
    else:
        print('Please enter "Y" or "n" ')
        return exit_()


def xpPoints():
    percentage = (num_correct/(num_correct + num_wrong))*100
    print('Total Correct: ' + str(num_correct) + '\n'
          'Total Wrong:   ' + str(num_wrong) + '\n'
          'Total XP:      ' + str(xp_total) + '\n'
          'Percentage:    ' + str(percentage))
    return game()


def AddProb(addQuestion, addAnswer):
    if input(addQuestion + ' ') == addAnswer:
        return True


def addition():
    print('You chose Addition! ')
    global num_correct
    global num_wrong
    global xp_total
    correct = 0
    wrong = 0
    xp = 0
    counter = 0
    while (counter < 10):
        random.shuffle(additionList)
        for addQuestion, addAnswer in additionList:
            if AddProb(addQuestion, addAnswer):
                num_correct += 1
                xp_total += 1
                correct += 1
                xp += 1
                print('[+] Correct! + 1xp')
                break
            else:
                print('[-] Wrong! ')
                num_wrong += 1
                wrong += 1
                break
        counter += 1
    print('\n'
          'Number Wrong:   ' +str(wrong) +'\n'
          'Number Correct: ' + str(correct) +'\n'
          'XP Gained:      ' + str(xp))
    game()

def SubProb(subQuestion, subAnswer):
    if input(subQuestion + ' ') == subAnswer:
        return True


def subtraction():
    print('You chose Subtraction! ')
    global num_correct
    global num_wrong
    global xp_total
    correct = 0
    wrong = 0
    xp = 0
    counter = 0
    while (counter < 10):
        random.shuffle(subtractionList)
        for subQuestion, subAnswer in subtractionList:
            if SubProb(subQuestion, subAnswer):
                num_correct += 1
                xp_total += 1
                correct += 1
                xp += 1
                print('[+] Correct! + 1xp ')
                break
            else:
                print('[-] Wrong! ')
                num_wrong += 1
                wrong += 1
                break
        counter += 1
    print('\n'
          'Number Wrong:   ' +str(wrong) +'\n'
          'Number Correct: ' + str(correct) +'\n'
          'XP Gained:      ' + str(xp))
    game()

additionList = [('11 + 11', '22'),
                ('11 + 2', '13'),
                ('11 + 3', '14'),
                ('11 + 4', '15'),
                ('11 + 5', '16'),
                ('11 + 6', '17'),
                ('11 + 7', '18'),
                ('11 + 8', '19'),
                ('11 + 9', '20'),
                ('12 + 2', '14'),
                ('12 + 3', '15'),
                ('12 + 4', '16'),
                ('12 + 5', '17'),
                ('12 + 6', '18'),
                ('12 + 7', '19'),
                ('12 + 8', '20'),
                ('12 + 9', '21'),
                ('3 + 3', '6'),
                ('3 + 4', '7'),
                ('3 + 5', '8'),
                ('3 + 6', '9'),
                ('3 + 7', '10'),
                ('3 + 8', '11'),
                ('3 + 9', '12'),
                ('4 + 4', '8'),
                ('4 + 5', '9'),
                ('4 + 6', '10'),
                ('4 + 7', '11'),
                ('4 + 8', '12'),
                ('4 + 9', '13'),
                ('5 + 5', '10'),
                ('5 + 6', '11'),
                ('5 + 8', '13'),
                ('5 + 9', '14'),
                ('6 + 6', '12'),
                ('6 + 7', '13'),
                ('6 + 8', '14'),
                ('6 + 9', '15'),
                ('7 + 7', '14'),
                ('7 + 8', '15'),
                ('7 + 9', '16'),
                ('8 + 8', '16'),
                ('8 + 9', '17'),
                ('9 + 9', '18'),
                ('10 + 4', '14'),
                ('10 + 5', '15'),
                ('10 + 6', '16'),
                ('10 + 7', '17'),
                ('10 + 8', '18'),
                ('10 + 9', '19'),
                ('10 + 10', '20'),
                ('13 + 3', '16'),
                ('13 + 4', '17'),
                ('13 + 5', '18'),
                ('13 + 6', '19'),
                ('13 + 7', '20'),
                ('13 + 8', '21'),
                ('13 + 9', '22'),
                ('13 + 10', '23'),
                ('13 + 11', '24'),
                ('13 + 12', '25'),
                ('13 + 13', '26'),
                ]

subtractionList = [('9 - 1', '8'),
                   ('9 - 2', '7'),
                   ('9 - 3', '6'),
                   ('9 - 4', '5'),
                   ('9 - 5', '4'),
                   ('9 - 6', '3'),
                   ('9 - 7', '2'),
                   ('9 - 8', '1'),
                   ('9 - 9', '0'),
                   ('8 - 1', '7'),
                   ('8 - 2', '6'),
                   ('8 - 3', '5'),
                   ('8 - 4', '4'),
                   ('8 - 5', '3'),
                   ('8 - 6', '2'),
                   ('8 - 7', '1'),
                   ('8 - 8', '0'),
                   ('17 - 1', '16'),
                   ('17 - 2', '15'),
                   ('17 - 3', '14'),
                   ('17 - 4', '13'),
                   ('17 - 5', '12'),
                   ('17 - 6', '11'),
                   ('17 - 7', '10'),
                   ('16 - 1', '15'),
                   ('16 - 2', '14'),
                   ('16 - 3', '13'),
                   ('16 - 4', '12'),
                   ('16 - 5', '11'),
                   ('16 - 6', '10'),
                   ('5 - 1', '4'),
                   ('5 - 2', '3'),
                   ('5 - 3', '2'),
                   ('5 - 4', '1'),
                   ('5 - 5', '0'),
                   ('4 - 1', '3'),
                   ('4 - 2', '2'),
                   ('4 - 3', '1'),
                   ('4 - 4', '0'),
                   ('3 - 1', '2'),
                   ('3 - 2', '1'),
                   ('3 - 3', '0'),
                   ('12 - 10', '2'),
                   ('12 - 2', '10'),
                   ('12 - 11', '1'),
                   ('12 - 9', '3'),
                   ('12 - 8', '4'),
                   ('12 - 7', '5'),
                   ('12 - 6', '6'),
                   ('12 - 5', '7'),
                   ('12 - 4', '8'),
                   ('12 - 3', '9'),
                   ('12 - 2', '10'),
                   ('12 - 1', '11'),
                   ]


if __name__ == '__main__':
    game(prompt)
