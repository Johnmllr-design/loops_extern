# this is for task two of the loops project assigned in the externship module

num = int(input("what is your value"))      # get the value
copy = num
i = num - 1

while i > 1:                                # loop while i > 1 to sum up the factorial
    num = num * i
    i -= 1

print("the factorial of " + str(copy) + " is " + str(num))      # print a message