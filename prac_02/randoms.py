import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# 8

# What was the smallest number you could have seen, what was the largest?
# smallest is 5, largest is 19


# What did you see on line 2?
# 9

# What was the smallest number you could have seen, what was the largest?
# smallest is 3, largest is 9


# Could line 2 have produced a 4?
# no


# What did you see on line 3?
# 5.015425844557204

# What was the smallest number you could have seen, what was the largest?
# smallest is 2.5, largest is 5.4

print('-----------')

def main():
    print(random.randint(1, 100))

main()