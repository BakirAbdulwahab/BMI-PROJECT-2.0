height = float(input("Please enter your height in Meters(m): "))
weight = float(input("Please enter your weight in Kilograms(kg): "))

equation = weight / height**2

if equation < 18.5:
    print("You are underweight.")
elif equation < 25:
    print("You are normal weight.")
elif equation < 30:
    print("You are overweight.")
elif equation < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")