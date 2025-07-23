1.

class my_class:
     x = 5
 p1 = my_class()
 print(p1.x)

2.

 class person():
      def __init__(self, name, age):
          self.name = name
          self.age = age
 p1=person("Reetak", 20)
 print(p1.name + " is " + str(p1.age) + " years old.")

3.

class delta():
     def __init__(self, roll_no, name):
         self.roll_no = roll_no
         self.name = name
 p1=delta("h240121", "Reetak")
 print(p1.roll_no + " is the roll number of " + p1.name + ".")

4.

 class person():
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def display(self):
         print(f"{self.name} is {self.age} years old.")
 p1 = person("Reetak", 20)
 p1.display()


5.

 class faculty:  # created a class 
     total_faculty=0 
     def __init__(self , name , department):
         self.name = name
         self.department = department
         faculty.total_faculty += 1
     @classmethod
     def total(cls):  # here cls give refrence or define class .
         print(f"total no of faculty members : {cls.total_faculty}")
 f1 = faculty("reetak" , " cse ")
 f2 = faculty("jatin" , " cse ")
 f3 = faculty("adii" , "ce ")

 faculty.total()


6.        

class main:
     def __init__(self, name):
         self.name = name

 class student(main):
     def __init__(self, name, roll_no):
         super().__init__(name)
         self.roll_no = roll_no
         print(f"hello {self.name} , Your roll number is {self.roll_no}.")
 s1 = student("Reetak", "h240121")
 s2 = student("Jatin", "h240122")
 s3 = student("Adii", "h240123")


7.

class main:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def display(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")
m1 = main("Reetak", 20)
m1.set_age(25)


8.

class main:
    def __init__(self, name):
        self.name = name

class result(main):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

a1 = result("vostro 3400", "dell")
print(f"{a1.name} is a laptop of {a1.model} model!")

