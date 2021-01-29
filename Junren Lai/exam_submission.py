"""
CP1401 2020-1 Final Exam - Online Assignment
Name: Lai Junren

Where needed, use additional code files.
Ensure that each question's answer is clearly identifiable.
"""

# 7.
# once you enter the loop, you should print x first. If you print x/2 immediately, you skip the value 16.
# Explanation:
# 1. X doesn't change, so it's stuck in an infinite loop and it doesn't come out
# 2. X /2 is a floating-point number that needs to be divisible or converted to an integer to be printed
# 3. Once you enter the loop, you should print x first. If you print x/2 immediately, you skip the value 16
# Code:
# This loop should count down from 100 to 0 in steps of 5
x = 16
while x > 0:
    print(x)
    x //= 2

# 8.
# Explanation:
# 1. After you modify an element in the list, no value is assigned back to the list, so the element in the list does not change its value

# Code:
# Start with lowercase state names
things = ["qld", "nsw", "act"]
print("Original:", things)

# Make them uppercase
for i in range(len(things)):
    thing = things[i].upper()
    things[i] = thing
print("Uppercase names now:", things)


# 9.
# Code:
def main():
    try:
        in_file = open("data.txt")
        data = get_data(in_file)
        in_file.close()
        avg = average(data)
        print("The average is ", avg)
    except:
        print("File Open failed!")


def get_data(in_file):
    values = []
    for line in in_file:
        try:
            values.append(float(line.strip()))
        except:
            pass
    return values


def average(data):
    if data is None or len(data) <= 0:
        return 0.0
    return sum(data) / len(data)


main()

# Explanation:
# 1. To open the file, add try.. Except statement to prevent the program from crashing if the file does not exist
# 2. Try should be added to each row converted to float. Except statement to prevent program crashes caused by non-numeric rows
# 3. The average function is designed to take a list of floats and average them. The length of the list can be calculated without passing it in
# 4. Data is handled as a non - null judgment to prevent 0 - divisor exceptions
# 5. Average does not need to be responsible for printing, but only needs to calculate the average value and return it. The printing step is handled by main function

# 10.
age = -1
while age < 0 or age > 120:
    try:
        age = int(input("Age: "))
        if age < 0 or age > 120:
            print("Age must be between 0 and 120")
        else:
            break
    except:
        print("Invalid integer")
print("In 10 years, you will be " + str(age + 10))


# 11.
def function(x, y=1, z=10):
    return x + y + z


print(function(2, y=5))  # prints 17
print(function(100))  # prints 111

# 12.
d = {4: "good", 1: "hello", 5: "subject", 2: "welcome", 3: "exam"}
d_items = sorted(d.items(), key=lambda x: x[1])
for k, v in d_items:
    print(v + " is " + str(k))

# 13.
data_string = "date='12/11/2020', temperature='23.1c', uv='6.43'"
data_string = "uv='11.05', date='01/10/2019', temperature='9.7c'"

temperature = data_string.split("temperature='")[1].split("c'")[0]

# 14.
numbers = [10, 21, -10, 103, -20, 200, 111, -300, 99]
print(numbers[-1])
print(numbers[2:5])
print(numbers[2::2])
print(numbers[::-1])
print("The odd numbers are " + str([num for num in numbers if num % 2 == 1]))
print("There are " + str(len(numbers)) + " numbers")

# 15.
pairs = ((2351, 'g'), (127.125, 'kg'), (734, 'g'), (12.931, 'kg'), (108.22, 'kg'))
for pair in pairs:
    weight = pair[0]
    unit = pair[1]
    converted_str = ""
    if unit == "g":
        weight_converted = weight / 1000
        converted_str = " (converted)"
    else:
        weight_converted = weight
    print("%8s -> %8.1f kg%s." % (weight, weight_converted, converted_str))

# 16.
names = ["Jimmy", "Alison", "Katherina", "Bob"]
for index, name in enumerate(names):
    print("{}. {} ({} characters)".format(index + 1, name, len(name)))

# 17.
values = [('Heidi', 3), ('Jack', 5), ('Abby', 3), ('Tim', 4)]
sort_values = sorted(values, key=lambda x: (x[1], x[0]))
new_values = ["{}-{}".format(number, string) for string, number in sort_values]
print(new_values)

# 18.
string = "aPPearance"  # ->  Your code should print "acenpr"
string = "coMmission"  # -> Your code should print "cimnos"

letters = []
for letter in string.lower():
    if letter not in letters:
        letters.append(letter)
letters.sort()
new_string = "".join(letters)
print(new_string)

# 19.
values = [7, 13, -6, -35, 24]
additions = [num + 5 for num in values]
pairs = [(index - len(values), num) for index, num in enumerate(values)]
signals = [1 if num > 0 else -1 for index, num in enumerate(values)]
print(additions)
print(pairs)
print(signals)

# 20. Answer in musicians.py
# 21. Answer in thing.py
# 22. Answer in stamps.py
