# Andrea Egan - Task 7
# This program reads in a text file 
# and outputs the number of e's it contains by using a 'for loop'
# The program will also take the filename from an argument on the command line.
# To create an argument, you must first import 'sys'. 
# sys is a list of commandline arguments, passed to the python programme.

import sys 

x = "e"
y = 0

with open ("moby-dick.txt", "r")as f: 
    if len(sys.argv) == 1:  
            FileName = (sys.argv[1]) 
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter==x):
                    y = y + 1
print (y)

# Reference: https://realpython.com/python-command-line-arguments/#the-sysargv-array
#          : https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162 
#          : https://www.tutorialspoint.com/python/python_command_line_arguments.htm 
#          : https://jakevdp.github.io/WhirlwindTourOfPython/07-control-flow-statements.html