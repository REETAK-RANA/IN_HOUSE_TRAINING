# Water Bottle Consumption Tracker

total_bottles = int(input("Enter total water bottles: "))
daily_drink = int(input("Enter bottles you drink per day: "))

day = 1

while total_bottles > 0:
    if total_bottles >= daily_drink:
        consumed = daily_drink
    else:
        consumed = total_bottles

    total_bottles -= consumed

    print(f"Day {day}: Drank {consumed} bottle{'s' if consumed > 1 else ''}. {total_bottles} left.")
    day += 1

print("No more bottles left!")
