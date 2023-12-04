# Basic - Print all integers from 0 to 150.
for i in range (0,151):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for multiple in range (5,1001,5):
    print(multiple)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".
for num in range (1,101):
    if num%10 ==0:
        print("Coding Dojo")
    elif num%5 == 0:
        print("Coding")
    else:
        print(num)
        
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# sum =0
for num1 in range (1,500000,2):
    sum += num1
    print(sum)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num2 in range (2018,0,-4):
    print(num2)
# Flexible Counter - Set three variables: lowNum, highNum,
#  mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
low= 2
high= 9
mult= 3

for x in range (low,high +1):
    if x%mult == 0:
        print(x)
