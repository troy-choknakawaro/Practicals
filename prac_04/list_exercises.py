# 1. Basic list operations
numbers = []
for i in range(5):
    num = int(input('Number: '))
    numbers.append(num)

print('The first number is {}'.format(numbers[0]))
print('The last number is {}'.format(numbers[4]))
print('The smallest number is {}'.format(min(numbers)))
print('The largest number is {}'.format(max(numbers)))
print('The average number is {}'.format(sum(numbers) / len(numbers)))

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input('Enter username: ')
if username in usernames:
    print('Access granted')
else:
    print('Access denied')