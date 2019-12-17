import os

def main():
    os.chdir("day7")
    file = open("input.txt", "r")
    data = file.readline().split(",")
    
    maxSignal = 0
    maxSequence = [0,0,0,0,0]

    for phaseA in range(5,10):
        for phaseB in range(5,10):
            for phaseC in range(5,10):
                for phaseD in range(5,10):
                    for phaseE in range(5,10):
                        phaseAmplifiers = [phaseA, phaseB, phaseC, phaseD, phaseE]
                        if len(phaseAmplifiers) == len(set(phaseAmplifiers)): # if there are no duplicates (unique nums from 0 to 4)
                            signalAmt = outputSignal(data, phaseAmplifiers)
                            if signalAmt > maxSignal:
                                maxSignal = signalAmt
                                maxSequence = phaseAmplifiers.copy()

    print(maxSignal)
    print(maxSequence)

def outputSignal(theData, amplifiers):
    backup = theData.copy()
    previousAmount = 0
    signalAmounts = [0, 0, 0, 0, 0]
    for i in range (0,len(signalAmounts)):
        theData = backup.copy()
        signalAmounts[i] = intcode(theData, amplifiers[i], previousAmount)
        previousAmount = signalAmounts[i]
    return signalAmounts[len(signalAmounts) - 1]

def intcode(theData, phaseSetting, incomingSignal):
    currentPosition = 0
    result = 0
    inputGiven = phaseSetting
    length = len(theData)

    while(currentPosition < length):
        instructionNum = 0
        
        command = int(theData[currentPosition]) % 100

        if command == 99:
            return result
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
            inputGiven = incomingSignal
            instructionNum = 2
        elif command == 4:
            result += int(theData[value1])
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

    return result

def get_digit(number, n):
    return number // 10**n % 10

if __name__== "__main__":
    main()