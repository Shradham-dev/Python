# 1. Create a "Person" class with name and age attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating two instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Display their details
person1.display()
person2.display()

# 2. Create a "Student" class with name and roll_no attributes
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# Creating an object of the Student class
student1 = Student("John", 2)

# Display student details
student1.display()

# 3. Define a class to represent a bank account
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Creating a bank account object and performing operations
account = BankAccount("Alice")
account.deposit(500)
account.withdraw(200)
account.check_balance()

# 4. Define a class "Student" with attributes like name and age
class StudentDetail:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating objects to represent different students
student2 = StudentDetail("Emma", 20)
student3 = StudentDetail("Liam", 22)

# Display student details
student2.display()
student3.display()
    