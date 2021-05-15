print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 20, 30? "))
people_nos = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip / people_nos
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")
