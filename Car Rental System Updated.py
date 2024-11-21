class Car:
    def __init__(self, car_id, brand, model, rent_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.is_rented = False
        self.rented_by = None  # To store the name of the customer
        self.rent_days = 0     # To store the number of days rented

    def display_info(self):
        status = f"Rented by {self.rented_by}" if self.is_rented else "Available"
        print(f"ID: {self.car_id} | Brand: {self.brand} | Model: {self.model} | Rent: ${self.rent_per_day}/day | Status: {status}")


class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            car.display_info()

    def rent_car(self, car_id, customer_name, days):
        for car in self.cars:
            if car.car_id == car_id:
                if not car.is_rented:
                    car.is_rented = True
                    car.rented_by = customer_name
                    car.rent_days = days
                    print(f"\nYou have successfully rented the {car.brand} {car.model} for {days} day(s).")
                else:
                    print("\nSorry, this car is already rented.")
                return
        print("\nCar ID not found.")

    def return_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_rented:
                    total_cost = car.rent_per_day * car.rent_days
                    print(f"\n{car.rented_by}, you have successfully returned the {car.brand} {car.model}.")
                    print(f"Total rental cost: ${total_cost}")
                    # Reset the car's status
                    car.is_rented = False
                    car.rented_by = None
                    car.rent_days = 0
                else:
                    print("\nThis car is not rented.")
                return
        print("\nCar ID not found.")

    def view_rental_info(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_rented:
                    print(f"\nCar {car.brand} {car.model} is rented by {car.rented_by} for {car.rent_days} day(s).")
                else:
                    print("\nThis car is currently available.")
                return
        print("\nCar ID not found.")


def main():
    rental_system = CarRentalSystem()

    # Adding some cars to the system
    rental_system.add_car(Car(1, "Toyota", "Camry", 50))
    rental_system.add_car(Car(2, "Honda", "Civic", 40))
    rental_system.add_car(Car(3, "Ford", "Mustang", 100))

    while True:
        print("\n--- Car Rental System ---")
        print("1. Display all cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. View rental info")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            rental_system.display_cars()
        elif choice == "2":
            car_id = int(input("\nEnter the Car ID to rent: "))
            customer_name = input("Enter your name: ")
            days = int(input("Enter number of days to rent: "))
            rental_system.rent_car(car_id, customer_name, days)
        elif choice == "3":
            car_id = int(input("\nEnter the Car ID to return: "))
            rental_system.return_car(car_id)
        elif choice == "4":
            car_id = int(input("\nEnter the Car ID to view rental info: "))
            rental_system.view_rental_info(car_id)
        elif choice == "5":
            print("\nThank you for using the Car Rental System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
