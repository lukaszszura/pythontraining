print("Welcome to the Pizza Order")
size = input("What size pizza do you want? S, M or L: ")
peperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_s = 2
pepperoni_m_l = 3
cheese_s_m_l = 1

bill = 0 
if size == "S":
    bill = small_pizza
elif size == "M":
    bill = medium_pizza
else:
    bill = large_pizza

if peperoni == "Y":
   if size == "S":
    bill = bill + pepperoni_s
   else:
    bill = bill + pepperoni_m_l

if cheese == "Y":
    bill = bill + cheese_s_m_l

print(f"Your piiza bill is ${bill}.")