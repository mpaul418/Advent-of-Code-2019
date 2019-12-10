import os

def main():
    os.chdir('day3')
    file = open('input.txt', 'r')
    wire1 = file.readline().split(',')
    wire2 = file.readline().split(',')

    wire1Lines = createGrid(wire1)
    wire2Lines = createGrid(wire2)
    minManhattanDistance = -1
    fewestSteps = -1

    wire1Steps = 0
    for i in range(len(wire1Lines) - 1):
        wire2Steps = 0
        for j in range(len(wire2Lines) - 1):
            if i == 0 and j == 0:
                continue
            if (wire1[i][0] == 'L' or wire1[i][0] == 'R') != (wire2[j][0] == 'L' or wire2[j][0] == 'R'):
                intersection = findIntersection(wire1Lines[i], wire1Lines[i + 1], wire2Lines[j], wire2Lines[j + 1])
                if intersection[0] != -1:
                    # Part 1 calculations
                    if minManhattanDistance < 0 or (abs(intersection[0]) + abs(intersection[1]) < minManhattanDistance):
                        minManhattanDistance = abs(intersection[0]) + abs(intersection[1])
                    # Part 2 calculations
                    stepDistance = wire1Steps + wire2Steps
                    if wire1[i][0] == 'L' or wire1[i][0] == 'R':
                        stepDistance += abs(wire1Lines[i][0] - intersection[0]) + abs(wire2Lines[j][1] - intersection[1])
                    else:
                        stepDistance += abs(wire1Lines[i][1] - intersection[1]) + abs(wire2Lines[j][0] - intersection[0])
                    if fewestSteps < 0 or stepDistance < fewestSteps:
                        fewestSteps = stepDistance
            wire2Steps += int(wire2[j][1:])
        wire1Steps += int(wire1[i][1:])

    print(minManhattanDistance)
    print(fewestSteps)
    
def findIntersection(segment1Start, segment1End, segment2Start, segment2End):
    if segment1Start[0] != segment1End[0]: # if wire 1 is moving horizontally
        # x0 -> x1 must intersect other x and y0 -> y1 must intersect other y
        if (segment1Start[0] - segment2Start[0] > 0) != (segment1End[0] - segment2Start[0] > 0): # if the horizontal distance can intersect
            if (segment2Start[1] - segment1Start[1] > 0) != (segment2End[1] - segment1Start[1] > 0): # if the vertical distance can intersect
                return (segment2Start[0], segment1Start[1])
    else: # wire 1 is moving vertically
        # x0 -> x1 must intersect other x and y0 -> y1 must intersect other y
        if (segment2Start[0] - segment1Start[0] > 0) != (segment2End[0] - segment1Start[0] > 0): # if the horizontal distance can intersect
            if (segment1Start[1] - segment2Start[1] > 0) != (segment1End[1] - segment2Start[1] > 0): # if the vertical distance can intersect
                return (segment1Start[0], segment2Start[1])

    return (-1, -1)

def createGrid(wire):
    result = [(0,0)]
    lastX = 0
    lastY = 0

    for segment in wire:
        direction = segment[:1]
        distance = segment[1:]
        if direction == 'R':
            result.append((lastX + int(distance), lastY))
            lastX += int(distance)
        elif direction == 'L':
            result.append((lastX - int(distance), lastY))
            lastX -= int(distance)
        elif direction == 'U':
            result.append((lastX, lastY + int(distance)))
            lastY += int(distance)
        elif direction == 'D':
            result.append((lastX, lastY - int(distance)))
            lastY -= int(distance)

    return result

if __name__== '__main__':
    main()