"""Stamps question"""
import random

from stamp import Stamp


def main():
    stamps = read_stamps("stamp_data.txt")
    stamps_count = len(stamps)
    rare_count = 0
    countries = []
    for stamp in stamps:
        if stamp.is_rare:
            rare_count += 1
        if stamp.country not in countries:
            countries.append(stamp.country)
    print("You have {} stamps ({} rare).".format(stamps_count, rare_count))
    if stamps_count > 0:
        print("The highest denomination of your stamps is $%.2f" % sorted(stamps)[-1].denomination)
    print("You have stamps from these {} countries:".format(len(countries)))
    print(", ".join(countries))
    print("Today's random stamp is:")
    random_stamp = random.choice(stamps)
    print(random_stamp)


def read_stamps(file_name):
    try:
        file = open(file_name)
        stamps = []
        for line in file:
            line = line.strip()
            parts = line.split(",")
            country = parts[0]
            if parts[1].endswith("*"):
                denomination = float(parts[1][:-1])
                is_rare = True
            else:
                denomination = float(parts[1])
                is_rare = False
            stamps.append(Stamp(country, denomination, is_rare))
        file.close()
        return stamps
    except Exception as e:
        print(e)
        return []


main()
