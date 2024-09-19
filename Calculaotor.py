# def calculate_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     return bmi

# # Get user input
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# # Calculate BMI
# bmi = calculate_bmi(weight, height)

# # Display the result
# print(f"Your BMI is: {bmi:.2f}")

# # Optional: BMI category
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight/(height**2)
if bmi<18.5:
    print("your are underweight")
elif bmi<25:
    print("you have a normal weigth")
elif bmi<30:
    print("you are slightly overweight")
elif bmi <35:
    print("your are obese")
else:
    print("invalid")