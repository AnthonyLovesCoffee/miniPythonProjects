import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, colourArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, colourArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

    drawData(data, colourArray(len(data), head, tail, border, tail, True))
    data[border], data[tail] = data[tail], data[border]

    return border

def quickSort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitioni = partition(data, head, tail, drawData, timeTick)
        # left partition
        quickSort(data, head, partitioni - 1, drawData, timeTick)

        quickSort(data, partitioni + 1, tail, drawData, timeTick)


def colourArray(dataLen, head, tail, border, currentindx, isSwapping=False):
    colourArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colourArray.append("grey")
        else:
            colourArray.append("white")
        
        if i == tail:
            colourArray[i] = 'blue'
        elif i == border:
            colourArray[i] = 'red'
        elif i == currentindx:
            colourArray[i] = 'yellow'

        if isSwapping:
            if i == border or i == currentindx:
                colourArray[i] = 'green'

    return colourArray
