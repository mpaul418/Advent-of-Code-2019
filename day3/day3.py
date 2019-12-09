import os

def main():
    os.chdir('day3')
    file = open('input.txt', 'r')
    wire1 = file.readline().split(',')
    wire2 = file.readline().split(',')

    wire1Lines = createGrid(wire1)
    wire2Lines = createGrid(wire2)

    #TODO check for intersections- only call on segments that are going one horizontal and one vertical
    
def isIntersection(segment1Start, segment1End, segment2Start, segment2End):
    #TODO (assume that segments can intersect)

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