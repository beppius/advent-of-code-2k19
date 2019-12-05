import math


def total_fuel():
    inputFile = open("hint_exc_1.txt", "r")

    answer = 0
    for i in inputFile:
        mass = int(i)
        fuel = (math.trunc(mass / 3)) - 2
        answer = answer + fuel
    print(answer)
    inputFile.close()


def total_fuel_part2():
    inputFile = open("hint_exc_1.txt", "r")

    answer = 0
    for i in inputFile:
        mass = int(i)
        fuel = (math.trunc(mass / 3)) - 2
        fuelTotal = fuel
        while fuel > 0:
            fuel = (math.trunc(fuel / 3)) - 2
            if fuel > 0:
                fuelTotal = fuelTotal + fuel
        answer = answer + fuelTotal

    print(answer)

    inputFile.close()
