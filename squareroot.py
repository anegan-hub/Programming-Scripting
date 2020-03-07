# Andrea Egan Task 6
# This program calculates the approximate square root of a positive number
# using a function based on Newtons method 

def sqrt (x): # creation of the function 'sqrt'
    est = x # estimated guess 
    y = 0 
    
    while x > y: # while the input is greater than zero
        est2 = (est - (est **2 - x) / (2 * est)) / 2

        # new variable which muiltples a negative number with
        # -1 to return the positive number
        m = est2 - est 
        if m < 0:   
            m *= -1

        est = est2
        return est

x = float(input("Please input a positive number: "))

print ("the squareroot of" , x , "is approx" , sqrt (x))

# Reference https://www.youtube.com/watch?v=tUFzOLDuvaE
# https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf

