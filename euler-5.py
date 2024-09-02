print ("Smallest Multiple")

'''
1. If we increment by 1 in the loop, it takes 5min to get the answer.
2. If we increment by 20 in the loop, it takes 13sec to get the answer. 

'''


num = 20
found = False
while found == False:
    mod_num = 2
    while mod_num < 21:
        if num % mod_num != 0:
            break
        mod_num += 1
    if mod_num == 21:
        print(num)
        found = True
    num += 20


