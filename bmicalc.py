# input height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Specify data type for height and wight
weight_as_int = float(weight)
height_as_float = float(height)

# BMI calculation
bmi = weight_as_int / height_as_float ** 2

# saved bmi as integer
bmi_as_int = int(bmi)

# Print bmi results
print(bmi_as_int)
