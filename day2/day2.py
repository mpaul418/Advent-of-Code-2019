import os

def main():
    os.chdir("day2")
    file = open("input.txt", "r")
    data = file.readline().split(",")
    data[1] = 12
    data[2] = 2
    currentPosition = 0
    while(currentPosition < len(data)):
        if int(data[currentPosition]) == 1:
            firstNum = int(data[int(data[currentPosition + 1])])
            secondNum = int(data[int(data[currentPosition + 2])])
            data[int(data[currentPosition + 3])] = str(firstNum + secondNum)
        elif int(data[currentPosition]) == 2:
            firstNum = int(data[int(data[currentPosition + 1])])
            secondNum = int(data[int(data[currentPosition + 2])])
            data[int(data[currentPosition + 3])] = str(firstNum * secondNum)
        elif int(data[currentPosition]) == 99:
            break
        else:
            print("error happened\n")

        currentPosition += 4

    print(str(data[0]))

if __name__== "__main__":
    main()