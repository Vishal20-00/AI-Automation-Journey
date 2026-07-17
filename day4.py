Weight = float(input("Please Entre your weight."))
Height = float(input("Please Entre your Height."))
bmi = Weight / (Height * Height)
print("Your bmi value is", round(bmi,2))
if bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Healthy")
else:
    print("Underweight")