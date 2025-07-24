# Q1 Create a function greet(name) that prints “Hello, [name]!” .
def greeting(name):
    print("Hello, " + name )
greeting("REETAK RANA")

#Q2. Create a function add(a, b) that returns the sum of two numbers. Call the function with inputs.
def add(a,b):
   a=int(input("Enter first number: "))
   b=int(input("Enter second number: "))
   return a + b
print("The sum is:", add(a,b))  


#Q3. Create a function display(*args) that accepts multiple arguments and prints them.
def delta(*jatin):
        print(f"my name is {jatin}")
delta("Reetak","Rana")


#Q4. Create a function student_info(**kwargs) that accepts name, age, roll number as keyword arguments and prints them.
def delta(**jatin):
        print(f"my name is {jatin}")
delta("Reetak":"Rana")


#Q5. create a function to check wheater a function is even or odd .
def delta(x):
    if x % 2 == 0:
        return " even "
    else:
        return " odd "

a = delta(input(" enter a number ")
print(a)
