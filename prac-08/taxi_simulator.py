from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def get_user_select():
    """
    Get User Valid Select
    :return:
    """
    valid_selects = ["q", "c", "d"]
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        select = input(">>> ").lower()
        if select in valid_selects:
            return select
        else:
            print("Invalid option")


def show_cars(cars):
    """
    Show every car
    :param cars:
    :return:
    """
    for i in range(len(cars)):
        print("{} - {}".format(i, cars[i]))


def get_choose_car(cars):
    """
    Get the car user chosen
    :param cars:
    :return:
    """
    while True:
        print("Taxis available: ")
        show_cars(cars)
        car_index = int(input("Choose taxi: "))
        if 0 <= car_index < len(cars):
            return cars[car_index]
        print("Invalid input")


def main():
    # total bill
    total_cost = 0
    # Generate three cars
    cars = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    # Current operate car
    cur_car = None
    print("Let's drive!")
    user_select = get_user_select()
    while user_select != "q":
        if user_select == "c":
            # Choose a car
            cur_car = get_choose_car(cars)
        elif user_select == "d":
            # Drive a car
            if cur_car is None:
                print("You should choose a taxi first!")
            else:
                cur_car.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                cur_car.drive(distance_to_drive)
                trip_cost = cur_car.get_fare()
                print("Your {} trip cost you ${:.2f}".format(cur_car.name, trip_cost))
                total_cost += trip_cost
        print("Bill to date: ${:.2f}".format(total_cost))
        user_select = get_user_select()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    show_cars(cars)


main()
