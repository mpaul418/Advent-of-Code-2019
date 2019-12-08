def main():
    total = 0
    part2Fuel = 0
    file = open("input.txt", "r")
    for line in file:
        currentAddition = int(int(line) / 3) - 2
        total += currentAddition
        currentAddition = int(int(currentAddition) / 3) - 2
        while(currentAddition > 0):
            total += currentAddition
            part2Fuel += currentAddition
            currentAddition = int(int(currentAddition) / 3) - 2
         
    print("Total fuel required (for part 1): " + str(total - part2Fuel))
    print("Total fuel required (for part 2): " + str(total))

if __name__== "__main__":
    main()