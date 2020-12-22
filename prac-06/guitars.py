from guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitars = []

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(str(guitar) + " added.")
        guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:  # lists, strings and other collections are False when empty, True when non-empty
        # In order for sorting to work on Guitar objects,
        # at least the __lt__ method must be defined in Guitar class
        guitars.sort()
        print("These are my guitars:")
        i = 1
        for guitar in guitars:
            is_vintage = ""
            if guitar.is_vintage():
                is_vintage = "(vintage)"
            print("Guitar {}: {} ({}), worth $ {:.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, is_vintage))
            i += 1
    else:
        print("No any guitars.")


main()
