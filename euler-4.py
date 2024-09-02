print("hello world")

def isPalindrome(num):
    num_copy = num
    reversed_num = []
    while num_copy > 0:
        remainder = num_copy % 10
        reversed_num.append(remainder)
        num_copy = num_copy//10
    
    new_number = 0
    for digits in reversed_num:
        new_number = new_number * 10
        new_number += digits
    
    if new_number == num:
        return True
    else:
        return False
    
largest = 0
value = 0
for a in reversed(range(100,1000)):
    for b in reversed(range(100,1000)):
        product = a*b
        value = isPalindrome(product) 
        if value is True:
            if largest < product:
                print(product,a,b)
                largest = product
            

