while True:
    print("\nMarriage Calculator")

    age1 = int(input("Enter your age: "))
    age2 = int(input("Enter partner's age: "))

    if age1 >= 18 and age2 >= 18:
        print("Both are eligible for marriage!")
    elif age1 >= 18 and age2 < 18:
        print(" Partner is not eligible for marriage yet.")
    elif age1 < 18 and age2 >= 18:
        print("You are not eligible for marriage yet.")
    else:
        print("Both are underage for marriage.")

    again = input("\nDo you want to check again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for checking! Stay smart and safe")
        break
