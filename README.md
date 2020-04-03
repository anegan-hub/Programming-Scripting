# Programming and Scripting Module 2020



# Introduction

This project relates to a programmimg and scripting module I am currently studying. All programs within the project, I have created based on the knowledge and skills I have gained during the semester. The project consist of 7 programs. Programmimg language is; python. 

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
- function plot.png


# Descriptions 


# BMI.py


This program is basesd on statements.
A statement is an instruction that the python interper can execute i.e 'print'. 

The program calculates a person's Body Mass Index (BMI)
Two variables are created as inputs; built in function float is used, as the input will be a floating number not an integar.



'''

    weight = float(input("Enter Weight in Kilograms: "))

    height = float(input("Enter Height in Centimeter "))

'''


A variable is then created called BMI. The variable takes the inputs and applies the calculation.

'''

      BMI = weight / ((height / 100)**2) 

    
'''


In addition to this, i included the if, elif, and  else function statements to categorise the result. 

Running the program on the command line you will be asked to input your weight and height. The output would look that this; 

'''


    λ python bmi.py

    Enter Weight in Kilograms: 53.5

    Enter Height in Centimeters: 162

    Your BMI is: 20.39. You are a Healthy weight



'''
# Secondstring.py

This programme will ask the user to input a string.
The output is every second character in reverse order.

Variable one


'''


    InputString = (input("Enter a sentence here: "))


'''


Variable two - using list indexing and slicing 

'''


    OutputString =  str. upper (InputString [::-2])


'''


The output of letters are in uppercase
solely to test the upper function. 


Output:

'''


    λ python secondstring.py


    Enter a sentence here: The quick brown fox jumps over the lazy dog.

    Every second character; capitalized; in reverse order is: .O ZLETRV PU O WR CU H


'''


