import os

class Amplifier:
    def __init__(self, data, phaseSetting):
        self.instrPtr = 0
        self.data = data
        self.phaseSetting = phaseSetting

    def intcode(self, incomingSignal):
        length = len(self.data)

        while(self.instrPtr < length):
            instructionNum = 0
            inputGiven = 0
            if(self.instrPtr == 0):
                inputGiven = self.phaseSetting
            else:
                inputGiven = incomingSignal
            
            command = int(self.data[self.instrPtr]) % 100

            if command == 99:
                return 0
            elif (command < 1 or command > 8):
                print("Broke at position " + str(self.instrPtr))
                return -1
            
            # determine immediate mode or position mode
            if get_digit(int(self.data[self.instrPtr]), 2) == 0 and (command == 1 or command == 2 or command > 4):
                value1 = int(self.data[int(self.data[self.instrPtr + 1])])
            else:
                value1 = int(self.data[self.instrPtr + 1])
            
            value2 = 0
            if self.instrPtr + 2 < length:
                if get_digit(int(self.data[self.instrPtr]), 3) == 0 and (command == 1 or command == 2 or command > 4):
                    value2 = int(self.data[int(self.data[self.instrPtr + 2])])
                else:
                    value2 = int(self.data[self.instrPtr + 2])

            value3 = 0
            if self.instrPtr + 3 < length:   
                value3 = int(self.data[self.instrPtr + 3])

            if command == 1:
                self.data[value3] = str(value1 + value2)
                instructionNum = 4
            elif command == 2:
                self.data[value3] = str(value1 * value2)
                instructionNum = 4
            elif command == 3:
                self.data[value1] = str(inputGiven)
                inputGiven = incomingSignal
                instructionNum = 2
            elif command == 4:
                self.instrPtr += 2
                return int(self.data[value1])
            elif command == 5:
                if value1 != 0:
                    self.instrPtr = value2
                else:
                    instructionNum = 3
            elif command == 6:
                if value1 == 0:
                    self.instrPtr = value2
                else:
                    instructionNum = 3
            elif command == 7:
                instructionNum = 4
                if value1 < value2:
                    self.data[value3] = 1
                else:
                    self.data[value3] = 0
            elif command == 8:
                instructionNum = 4
                if value1 == value2:
                    self.data[value3] = 1
                else:
                    self.data[value3] = 0   

            self.instrPtr += instructionNum

        return -2

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
    previousAmount = 0
    signalOutput = 0
    amplifierA = Amplifier(theData.copy(), amplifiers[0])
    amplifierB = Amplifier(theData.copy(), amplifiers[1])
    amplifierC = Amplifier(theData.copy(), amplifiers[2])
    amplifierD = Amplifier(theData.copy(), amplifiers[3])
    amplifierE = Amplifier(theData.copy(), amplifiers[4])
    
    while True:
        previousAmount = amplifierA.intcode(previousAmount)
        previousAmount = amplifierB.intcode(previousAmount)
        previousAmount = amplifierC.intcode(previousAmount)
        previousAmount = amplifierD.intcode(previousAmount)
        previousAmount = amplifierE.intcode(previousAmount)
        if previousAmount > 0:
            signalOutput = previousAmount
        else:
            break
    return signalOutput



def get_digit(number, n):
    return number // 10**n % 10

if __name__== "__main__":
    main()