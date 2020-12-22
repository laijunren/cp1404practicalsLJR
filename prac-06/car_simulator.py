from car import Car


def main():
    """Car simulator program, demonstrating use of Car class."""
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    # create a Car instance with initial fuel of 100 and user-provided name
    car = Car(car_name, 100)
    print(car)
    print_menu()
    select = input("Enter your choice: ").lower()
    while select != "q":
        if select == "d":
            drive(car)
        elif select == "r":
            refuel(car)
        else:
            print("Invalid choice")
        print()
        print(car)
        print_menu()
        select = input("Enter your choice: ").lower()
    print("\nGood bye {}'s driver.".format(car.name))


def print_menu():
    print("Menu:")
    print("d) drive")
    print("r) refuel")
    print("q) quit")


def drive(car):
    distance = int(input("How many km do you wish to drive? "))
    while distance < 0:
        print("Distance must be >= 0")
        distance = int(input("How many km do you wish to drive? "))
    distance = car.drive(distance)
    info = "The car drove {}km".format(distance)
    if car.fuel <= 0:
        info += " and ran out of fuel"
    info += "."
    print(info)


def refuel(car):
    fuel = int(input("How many units of fuel do you want to add to the car? "))
    while fuel < 0:
        print("Fuel amount must be >= 0")
        fuel = int(input("How many units of fuel do you want to add to the car? "))
    car.add_fuel(fuel)
    print("Added {} units of fuel.".format(fuel))


main()
