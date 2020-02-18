# Andrea Egan Task 5
# This is a program that will output
# whether or not today is a weekday.

import datetime
import calendar


DT = datetime.datetime.today()

print ("Today's Date: " , DT)

DT.day
print(DT.day) # returns the day (int)

DT.month      
print(DT.month) # returns the month (int)

DT.weekday() 
print(DT.weekday()) # returns the day of the week (0 = Monday)













