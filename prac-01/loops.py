# Displays all of odd numbers between 1 and 200
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars
star_number = int(input("Number of stars: "))
for i in range(star_number):
    print("*", end='')
print()

# d. print n lines of increasing stars
star_number = int(input("Number of stars: "))
for i in range(1, star_number + 1):
    for j in range(i):
        print("*", end='')
    print()
