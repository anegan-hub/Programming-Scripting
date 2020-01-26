# This program calculates a person's Body Mass Index (BMI)

weight = float(input("Enter Weight in Kilograms: "))
height = float(input("Enter Height in Centimeters: "))

# BMI Calculation:
BMI = weight / ((height / 100)**2) 

# BMI results calculation; for categorisation:

if BMI <= 18.5:
    print ("Your BMI is:" , str (round (BMI,2)) + ". You are Underweight")

elif BMI >= 18.5 and BMI <= 24.9:
    print ("Your BMI is:" , str (round (BMI,2)) + ". You are a Healthy weight")

elif BMI >= 25.0 :
    print ("Your BMI is:" , str (round (BMI)) + ". You are Overweight")

else:
    print ("Your BMI is:" , round (BMI,2))
