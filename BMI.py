weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
calculated_BMI = weight / height
print("Your calculated BMI is: ", calculated_BMI)
if calculated_BMI < 18.5:
    print("UnderWeight")
elif calculated_BMI > 18.5 and calculated_BMI < 24.9:
    print("HealthyWeight")
elif calculated_BMI > 25.0 and calculated_BMI < 29.9:
    print("OverWeight")
else:
    print("Obese")