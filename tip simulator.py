print("Restaurant Tip Simulator")

# Input the total bill and number of friends
bill_amount = float(input("Enter the total bill amount: ₹"))
friends = int(input("Enter number of friends splitting the bill: "))

# Calculate base split
split_amount = bill_amount / friends
print(f"Each person pays ₹{split_amount:.2f} before tip.")

# Choose tip percentage
print("\nChoose tip percentage:")
print("1. 10%")
print("2. 20%")
print("3. 30%")
print("4. 40%")
print("5. 50%")

tip_choice = int(input("Enter choice (1-5): "))

# Convert choice to actual percentage
tip_percent = tip_choice * 10

# Calculate tip and final per-person amount
tip_amount = (bill_amount * tip_percent) / 100
total_with_tip = bill_amount + tip_amount
final_split = total_with_tip / friends

print(f"\n💰 Tip selected: {tip_percent}%")
print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Total bill with tip: ₹{total_with_tip:.2f}")
print(f"Each person pays ₹{final_split:.2f} including tip.")
