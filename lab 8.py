# Question 1: Person and Student classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        self.display()
        print(f"Student ID: {self.student_id}")

# Demonstration
student = Student("Alice", 20, "S123")
student.show_details()

print("\n" + "=" * 50 + "\n")

# Question 2: Multilevel Inheritance with Vehicle, Car, and ElectricCar
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery")

# Demonstration
electric_car = ElectricCar()
electric_car.info()
electric_car.car_info()
electric_car.battery_info()

print("\n" + "=" * 50 + "\n")

# Question 3: Multiple Inheritance with Teacher, Author, and TutorAuthor
class Teacher:
    def description(self):
        print("I am a teacher. I educate students.")

class Author:
    def description(self):
        print("I am an author. I write books.")

class TutorAuthor(Teacher, Author):
    def description(self):
        print("As a TutorAuthor, I have dual responsibilities:")
        super().description()  # Calls the description method from the first parent class (Teacher)
        Author.description(self)  # Calls the description method from the Author class

# Demonstration
tutor_author = TutorAuthor()
tutor_author.description()

print("\n" + "=" * 50 + "\n")

# Question 4: Hierarchical Inheritance with Animal, Dog, and Cat
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Demonstration
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
