def is_armstrong_number(num):

    num_str = str(num)
    

    num_digits = len(num_str)
    

    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits
    

    return sum_of_digits == num


number = int(input("Enter a number: "))


if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
