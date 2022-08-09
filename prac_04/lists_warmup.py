numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# numbers[0] => 3
# numbers[-1] => 2
# numbers[3] => 1
# numbers[:-1] => [3, 1, 4, 1, 5, 9, 2]
# numbers[3:4] => [1]
# 7 in numbers => False
# "3" in numbers => False
# numbers + [6, 5, 3] => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(numbers)
print('--------')

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = 'ten'
print(numbers)
print('--------')

# Change the last element of numbers to 1
numbers[6] = 1
print(numbers)
print('--------')

# Get all the elements from numbers except the first two (slice)
numbers = numbers[2:]
print(numbers)
print('--------')

# Check if 9 is an element of numbers
numbers = 9 in numbers
print(numbers)


