weight = float(input("Enter weight"))
height = float(input("Enter height"))

bmi = weight / (height * height)

if bmi <= 18:
    print("Underweight")

elif bmi <= 29:
    print("Normal weight")
elif bmi <= 34:
    print("Overweight")
else:
    print("Obese")

