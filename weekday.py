# Andrea Egan Task 5
# This is a program that will output
# whether or not today is a weekday.
# To create the program, first you must import "datetime"
# This module supplies the dates and times.

import datetime

DT = datetime.datetime.now() 
days = (DT.isoweekday()) # Returns the day of the week where Monday is 1

if days <= 5:
    print ("Yes unfortunately today is a weekday")    
else:
    print ("Yah! It is the weekend")


# Reference https://jakevdp.github.io/WhirlwindTourOfPython