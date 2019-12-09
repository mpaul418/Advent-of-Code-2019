import os

def main():
    os.chdir("day2")
    file = open("input.txt", "r")
    data = file.readline().split(",")
    backup = data.copy()

    print("Part 1 answer: " + str(intcode(data, 12, 2)))

    for i in range(0, 100):
        for j in range(0, 100):
            data = backup.copy()
            if int(intcode(data, i, j)) == 19690720:
                print("Part 2 answer: " + str(100 * i + j))
                break

def intcode(theData, noun, verb):
    theData[1] = noun
    theData[2] = verb

    currentPosition = 0
    while(currentPosition < len(theData)):
        firstNum = int(theData[int(theData[currentPosition + 1])])
        secondNum = int(theData[int(theData[currentPosition + 2])])
        if int(theData[currentPosition]) == 1:
            theData[int(theData[currentPosition + 3])] = str(firstNum + secondNum)
        elif int(theData[currentPosition]) == 2:
            theData[int(theData[currentPosition + 3])] = str(firstNum * secondNum)
        elif int(theData[currentPosition]) == 99:
            break
        else:
            return -1

        currentPosition += 4

    return theData[0]

if __name__== "__main__":
    main()