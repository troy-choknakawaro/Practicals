try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# when input is string.

# When will a ZeroDivisionError occur?
# when input is 0.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# I could not, sorry.