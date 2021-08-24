print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What the procentage tip would youlike to give? 10, 12 or 15 "))
people = int(input("How many people to split bill?"))
tip_as_Procent = tip /100
total_tip = bill * tip_as_Procent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
