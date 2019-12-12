import os

def main():
    os.chdir("day5")
    file = open("input.txt", "r")
    data = file.readline().split(",")

    intcode(data)

def intcode(theData):
    currentPosition = 0
    length = len(theData)

    while(currentPosition < length):
        instructionNum = 0
        inputGiven = 5
        command = int(theData[currentPosition]) % 100

        if command == 99:
            break
        elif (command < 1 or command > 8):
            print("Broke at position " + str(currentPosition))
            return -1
        
        # determine immediate mode or position mode
        if get_digit(int(theData[currentPosition]), 2) == 0 and (command == 1 or command == 2 or command > 4):
            value1 = int(theData[int(theData[currentPosition + 1])])
        else:
            value1 = int(theData[currentPosition + 1])
        
        value2 = 0
        if currentPosition + 2 < length:
            if get_digit(int(theData[currentPosition]), 3) == 0 and (command == 1 or command == 2 or command > 4):
                value2 = int(theData[int(theData[currentPosition + 2])])
            else:
                value2 = int(theData[currentPosition + 2])

        value3 = 0
        if currentPosition + 3 < length:   
            value3 = int(theData[currentPosition + 3])

        if command == 1:
            theData[value3] = str(value1 + value2)
            instructionNum = 4
        elif command == 2:
            theData[value3] = str(value1 * value2)
            instructionNum = 4
        elif command == 3:
            theData[value1] = str(inputGiven)
            instructionNum = 2
        elif command == 4:
            print(theData[value1])
            instructionNum = 2
        elif command == 5:
            if value1 != 0:
                currentPosition = value2
            else:
                instructionNum = 3
        elif command == 6:
            if value1 == 0:
                currentPosition = value2
            else:
                instructionNum = 3
        elif command == 7:
            instructionNum = 4
            if value1 < value2:
                theData[value3] = 1
            else:
                theData[value3] = 0
        elif command == 8:
            instructionNum = 4
            if value1 == value2:
                theData[value3] = 1
            else:
                theData[value3] = 0   

        currentPosition += instructionNum

    return theData[0]

def get_digit(number, n):
    return number // 10**n % 10

if __name__== "__main__":
    main()