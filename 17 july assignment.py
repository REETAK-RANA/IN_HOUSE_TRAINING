def greeting(name):
    print("Hello, " + name )
greeting("REETAK RANA")

def add(a,b):
   a=int(input("Enter first number: "))
   b=int(input("Enter second number: "))
   return a + b
print("The sum is:", add(a,b))  # Call the function to see the result  


def delta(*jatin):
        print(f"my name is {jatin}")
delta("Reetak","Rana")

def delta(**jatin):
        print(f"my name is {jatin}")
delta("Reetak":"Rana")
