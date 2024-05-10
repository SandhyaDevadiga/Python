# If the bill was 150.00 rupees, split between 5 people, with 12 tip, Each person should pay (150/5)*1.12
# Round the result to 2 decimal places
print("Welcome to tip calculator")
bill=float(input("what was the total bill?"))
tip=int(input("what percentage tip would you like to give?10,20, 12, 15?"))
people=int(input("How many people to split the bill"))
tip_percent=tip/100
tip_amount=bill*tip_percent
total_bill=bill+tip_amount
bill_with_people=total_bill/people
final_ammount=round(bill_with_people,2)
print(f"Each person should pay {final_ammount}")