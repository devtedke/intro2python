#create two variables weight and height

weight = input("Enter weight")
height = input("Enter your height")

weight = int(weight)
height = int(height)

result = weight / (height * height)

print("Your BMI is ", result)