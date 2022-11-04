# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import re
from collections import Counter
def dice(user_input):
    result = re.split(r'[^56]', user_input)
    result_len = [len(a) for a in result if a != '']
    if(not result_len): return 0
    most_freq = Counter(result_len)
    return max([a for a in most_freq if most_freq[a]==max(most_freq.values())])
def dice_run(user_input):
    print(dice(user_input))
def checker(func, user_input, output):
    try:
        assert func(str(user_input)) == (output)
        print(f'Assertion of {func.__name__} on {user_input} passed')
    except AssertionError as err:
        print(f'Assertion of {func.__name__} on {user_input} failed, err')

checker(dice, 6556665, 7)
checker(dice, 5533661656, 2)
checker(dice, 1234, 0)
print("done with tests")
while 1:
    throws_result = input('Enter the result of throws: ')
    dice_run(throws_result)