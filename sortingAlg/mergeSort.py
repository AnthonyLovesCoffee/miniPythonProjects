import time


def mergeSort(data, drawData, timeTick):
    mergeAlg(data, 0, len(data)-1, drawData, timeTick)


def mergeAlg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        mergeAlg(data, left, middle, drawData, timeTick)
        mergeAlg(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, colourArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left : middle + 1]
    rightPart = data[middle + 1 : right + 1]

    lefti = righti = 0

    for datai in range(left, right+1):
        if lefti < len(leftPart) and righti < len(rightPart):
            if leftPart[lefti] <= rightPart[righti]:
                data[datai] = leftPart[lefti]
                lefti += 1
            else:
                data[datai] = rightPart[righti]
                righti += 1
        
        elif lefti < len(leftPart):
            data[datai] = leftPart[lefti]
            lefti += 1
        else:
            data[datai] = rightPart[righti]
            righti += 1
    
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def colourArray(dataLen, left, middle, right):
    colourArray = []

    for j in range(dataLen):
        if j >= left and j <= right:
            if j >= left and j <= middle:
                colourArray.append("purple")
            else:
                colourArray.append("blue")
        else:
            colourArray.append("white")
    return colourArray