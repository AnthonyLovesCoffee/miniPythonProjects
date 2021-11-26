# using tkinter for the GUI
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from quickSort import quickSort
from mergeSort import mergeSort

root = Tk()
root.title("Sorting Algorithm Visualiser")  # name of the GUI
root.maxsize(900, 600)  # max size of the root window
root.config(bg="white")  # background of window

# variables
selected_alg = StringVar()
data = []


# graphing the data
def drawData(data, colourArray):
    canvas.delete("all") # deletes the canvas everytime the function is called
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    # normalizing the data
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = colourArray[i])
        canvas.create_text(x0+2, y0, anchor= SW, text= str(data[i]), fill="white")
    root.update_idletasks()


def Generate():
    global data
    # getting the algorithm selected by the user
    print("Algorithm Selected: " + selected_alg.get())
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ["red" for x in range(len(data))])


def startAlgorithm():
    global data
    if not data: return

    if(algMenu.get()== "Quick Sort"):
        quickSort(data, 0, len(data)-1, drawData, speedScale.get())

    elif (algMenu.get() == "Bubble Sort"):
        bubbleSort(data, drawData, speedScale.get())
    
    elif (algMenu.get() == "Merge Sort"):
        mergeSort(data, drawData, speedScale.get())

    drawData(data, ["green" for x in range(len(data))])



# base layout
UI_frame = Frame(root, width=600, height=200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="black")
canvas.grid(row=1, column=0, padx=10, pady=5)

# UI Interface
# ROW[0]
Label(
    UI_frame, text="Algorithm: ", bg='grey'
    ).grid(row=0, column=0, padx=5, pady=5, sticky=W)

algMenu = ttk.Combobox(
    UI_frame, textvariable=selected_alg, values=["Bubble Sort", "Merge Sort", "Quick Sort"]
    )

algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)


speedScale = Scale(UI_frame, from_= 0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(
    UI_frame, text="Start", command=startAlgorithm, bg='green'
    ).grid(row=0, column=3, padx=5, pady=5)

# ROW[1]
sizeEntry = Scale(UI_frame, from_= 5, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(
    row=1, column=0, padx=5, pady=5,
    )

minEntry = Scale(UI_frame, from_= 0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(
    row=1, column=1, padx=5, pady=5,
    )

maxEntry = Scale(UI_frame, from_= 10, to=50, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(
    row=1, column=2, padx=5, pady=5,
    )

Button(
    UI_frame, text="Generate", command=Generate, bg='red'
    ).grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
