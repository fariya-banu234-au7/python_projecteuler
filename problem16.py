#Projecteuler - problem 16:

"""2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?"""


#To find the sum of the digits for any given number and its power input should be taken like this:
"""num = int(input("Enter the number: "))
x = int(input("Enter the power:  "))"""


#do this for this specific question where the num is fixed as 2 and power is taken as input from user
 
x = int(input("Enter the power:  "))
res = pow(2,x)
res = str(res)
ans = 0
for i in res:
    ans = ans + int(i)
print(ans)
