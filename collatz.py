# Andrea Egan - Task 4
# This program askes a user to input a positive intergar 
# Using the while loop to iterate through the intergar, not equal to 1
# The intergar is divided by 2 
# If that intergar is even, divide again by 2
# but if odd, multiply by 3, plus 1
# The program will end if the current integar is 1

p = int(input("Input a positive intergar: "))

while (p != 1): 
    if int (p % 2) == 0:
        p =  int (p / 2)
    else:
         p =  int ((p * 3) + 1) 
    print (p)  

print("Report complete")