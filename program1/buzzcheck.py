def is_buzz_number(num):
    return num % 7 == 0 or num % 10 == 7

number = int(input("Enter a number: "))

if is_buzz_number(number):
    print(number, "is a buzz number.")
else:
    print(number, "is not a buzz number.")
