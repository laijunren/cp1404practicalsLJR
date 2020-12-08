def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_num = int(input("How many months? "))

    for month in range(1, months_num + 1):
        income = float(input("Enter income for month {} : ".format(month)))
        incomes.append(income)

    print(get_income(months_num, incomes))


def get_income(months_num, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_num + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
