# Andrea Egan Task 5
# This is a program that will output
# whether or not today is a weekday.

import datetime

DT = datetime.datetime.now() 
days = (DT.isoweekday()) # weeks start with 1 

if days <= 5:
    print ("Yes unfortunately today is a weekday")    
else:
    print ("Yah! It is the weekend")