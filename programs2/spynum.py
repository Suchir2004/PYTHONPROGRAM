def is_spy_number(num):

    num_str = str(num)
    

    sum_of_digits = 0
    product_of_digits = 1
    for digit in num_str:
        digit = int(digit)
        sum_of_digits += digit
        product_of_digits *= digit
    
    
    return sum_of_digits == product_of_digits

number = int(input("Enter a number: "))

if is_spy_number(number):
    print(number, "is a spy number.")
else:
    print(number, "is not a spy number.")
