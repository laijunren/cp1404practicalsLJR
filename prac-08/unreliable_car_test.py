from unreliable_car import UnreliableCar


def main():
    uc = UnreliableCar("Unreliable Car", 100, 50)

    for i in range(10):
        print("The car wants to drive 10km")
        print("{} drives {}km.".format(uc.name, uc.drive(10)))
        print()

    print(uc)


if __name__ == '__main__':
    main()
