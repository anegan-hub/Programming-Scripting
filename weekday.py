# Andrea Egan Task 5
# This is a program that will output
# whether or not today is a weekday.

import datetime

DT = datetime.datetime.now() # Naive
 
#print ("Today's Date: " , DT)

DT.day
#print(DT.day) # returns the day (int)

DT.month      
#print (DT.month) # returns the month (int)

DT.year
#print (DT.year) # returns the year (int)

DT.isoweekday() 
#print(DT.isoweekday()) # returns the day of the week (1 = Monday) 

#print (DT.day , DT. month , DT. year ,)

dt1 = (DT.day , DT. month , DT. year )
#print ( " Today's Date: " , dt1)

Wd = (DT.isoweekday())

if Wd <= 5 :
    print (" Yes, unfortunaly today is a weekday")
else:
    print ("It is the weekend, yay!")
    



