from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)


if __name__ == '__main__':
    main()
