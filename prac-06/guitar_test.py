from guitar import Guitar

CURRENT_YEAR = 2017


def run_tests():
    """Tests for Guitar class."""

    guitar1 = Guitar("Guitar1", 1950, 9999.9)
    guitar2 = Guitar("Guitar2", 2002, 4999.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar1.name, 67,
                                                      guitar1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar2.name, 15,
                                                      guitar2.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name,
                                                         True,
                                                         guitar1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar2.name,
                                                         False,
                                                         guitar2.is_vintage()))


if __name__ == '__main__':
    run_tests()
