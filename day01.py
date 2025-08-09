from math import floor

data = []

with open("data/day01.txt", encoding="utf-8") as f:
    for line in f:
        data.append(int(line))


def calc_fuel(mass):
    return floor(mass / 3) - 2


def part1(data):
    total_fuel = []
    for i in data:
        total_fuel.append(calc_fuel(i))

    print(f"Part 1: {sum(total_fuel)}")


if __name__ == "__main__":
    part1(data)
