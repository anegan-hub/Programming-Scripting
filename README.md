# Programming and Scripting Module 2020



# Introduction

This project relates to a programming and scripting module I am currently studying. All programs within the project, I have created based on the knowledge and skills I have gained during the semester. The project consist of 7 programs. Programming language is; python. 

# Installations

The following software and tools were installed

- Anaconda
- Cmder
- Visual Studio Code 

# Useful Link

"https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf"

# Contents 

- bmi.py
- secondstring.py
- collatz.py 
- weekend.py
- squareroot.py
- es.py
- ipython_log.py
- function plot.png


# Descriptions 


# bmi.py


This program is basesd on statements.
A statement is an instruction that the python interper can execute i.e 'print'. 

The program calculates a person's Body Mass Index (BMI)
Two variables are created as inputs; built in function float is used, as the input will be a floating number not an integar.




    weight = float(input("Enter Weight in Kilograms: "))

    height = float(input("Enter Height in Centimeter "))




A variable is then created called BMI. The variable takes the inputs and applies the calculation.



    BMI = weight / ((height / 100)**2) 

    

In addition to this, i included the if, elif, and  else function statements to categorise the result. 

Running the program on the command line you will be asked to input your weight and height. The output would look that this; 




    λ python bmi.py

    Enter Weight in Kilograms: 53.5

    Enter Height in Centimeters: 162

    Your BMI is: 20.39. You are a Healthy weight




# secondstring.py

This programme will ask the user to input a string.
The output is every second character in reverse order.

Variable one




    InputString = (input("Enter a sentence here: "))




Variable two - using list indexing and slicing 



    OutputString =  str. upper (InputString [::-2])





The output of letters are in uppercase
solely to test the upper function. 


Output:



    λ python secondstring.py

    Enter a sentence here: The quick brown fox jumps over the lazy dog.

    Every second character; capitalized; in reverse order is: .O ZLETRV PU O WR CU H



# collatz.py


This program askes a user to input a positive intergar. Using the while loop to iterate through the intergar, not equal to 1. The intergar is divided by 2 , If that intergar is even, divide again by 2 but if odd, multiply by 3, plus 1. The program will end if the current integar is 1

Please note the indentations determine the body of the while loop




    While (p != 1):   
        if int (p % 2) == 0:
            p =  int (p / 2)
    else:
         p =  int ((p * 3) + 1) 
    print (p)  




So, the program above is stating 'while p is not equal to 1, if 2 divides into p evenly, divide again by 2 else P multiply by 3 and add one'.  

Output: 




    λ python collatz.py
    Input a positive intergar: 10
    5
    16
    8
    4
    2
    1
    Report complete





# weekend.py

This is a program that will output whether or not today is a weekday. To create the program, first you must import "datetime" This module supplies the dates and times.

Depending on how you what to run your program you can incorportate list, tubles and dictionaries. However i created a short program to produce the result i was looking for. 



    datetime.datetime.now() - # gives date with time in hours, minutes, seconds and milliseconds.

    (DT.isoweekday()) - # gives the starting weekday as 1 = monday. 




The program using the if and else statement, stats that if the variable days is less then 5 print " " else print " "


Output:




    λ python weekday.py

    Yes unfortunately today is a weekday




# squareroot.py 


This program calculates the approximate square root of a positive number by creating a function called 'sqrt'. The formula is based on Newtons Squareroot Method. 

The program runs however thr formula is still a working progress as the result is not returning the correct result. 

Reference https://en.wikipedia.org/wiki/Square_root
Reference https://www.youtube.com/watch?v=tUFzOLDuvaE


# es.py 

This program reads in a text file and outputs the number of e's it contains by using a 'for loop'. The program will also take the filename from an argument on the command line.
To create an argument, you must first import 'sys'. sys is a list of commandline arguments, passed to the python programme.


 The function noted below  with open, read and close a file





    with open ("moby-dick.txt", "r")as f: 





Argument




    if len(sys.argv) == 1:  
            FileName = (sys.argv[1]) 




The program has one argument that calls for the file name to be entered onto the commandline.
If the file name is not input, the report will not run. An Error message will appear on the commandline in this instance. 


For loop 



    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter==x):
                    y = y + 1



The for loop iterates over the given sequence, Here the program is breaking down the read file 'moby-dick.txt to count the number of 'e' within the file. 



# ipyton_log.py



IPython log file

This program displays a plot of the functions 
if(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
This program requires two imports 'numpy' and 'matplotlib.pyplot'.

import numpy as np

import matplotlib.pyplot as plt

    x = np.linspace(0, 4,) 

    g = x **2

    h = x **3


plt.plot(x, g, 'b.', label = "g(x)=x2") 

plt.plot(x, h, 'r.', label = "h(x)=x3")

plt.legend()

plt.title("Function Plot")

plt.xlabel("f(x)=x")

plt.ylabel("Y")

plt.show()
