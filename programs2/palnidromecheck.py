def is_palindrome(num):
    
    num_str = str(num)
    
    reversed_num_str = num_str[::-1]
    
    return num_str == reversed_num_str

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")
