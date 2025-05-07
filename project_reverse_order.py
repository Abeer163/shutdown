def count_digits(number):
    return len(str(abs(number)))

user_input = input("Enter a number to count its digits: ")
try:
    number = int(user_input)
    print(f"The number of digits in {number} is: {count_digits(number)}")
except ValueError:
    print("Please enter a valid integer.")
