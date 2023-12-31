import tkinter as tk

root = tk.Tk()
root.title("Viete-Paterns")
root.geometry("760x630")
root.geometry("820x630")


x1addx2 = 0
x1multiplyx2 = 0
kwadra = 0
znak = ""
OblDelta = 0

def EnterAll():
    global a
    a = entry1.get()
    a = int(a)

    global b
    b = entry2.get()
    b = int(b)   

    global c
    c = entry3.get()
    c = int(c)
   

def delta(a, b, c):
    global OblDelta
    OblDelta = (b*b)-4*a*c
    label4 = tk.Label(root, text=("Delta is equal to ", OblDelta), font=('Times', 16))
    label4.grid(row=4, column=0, columnspan=4, padx=5, pady=5)


def updateAll():
    labelx1_x2.config(text=("x1 + x2 = ", x1addx2))
    labelx1x2.config(text=("x1 * x2 = ", x1multiplyx2))
    
    labelx12x22.config(text=("x1^2 + x2^2 = ", kwadra))

    labelPosOrNeg.config(text="Are the numbers positive or negative")

    labelNumPosOrNeg.config(text=znak)


def MathAll(a, b, c):
    global x1addx2
    global x1multiplyx2
    x1addx2 = (-1 * b) / a
    x1multiplyx2 = c / a
    
    global kwadra
    kwadra = ((b*b) / (a*a)) - ((2 * c) / a)
    
    global znak
    if x1multiplyx2 < 0:
        znak = "Numbers x1, x2 have different signs"
        print("Numbers x1, x2 have different signs")
    elif x1addx2 > 0:
        znak = "x1 and x2 are positive"
        print("Numbers are positive")
    else:
        znak = "x1 and x2 are negative"
        print("Numbers are negative")

    updateAll()


def CountAll(a, b, c):
    delta(a, b, c)
    if OblDelta >=0:
        MathAll(a, b, c)
    else:
        pass


label1= tk.Label(root, text = "Enter a", font=('Times', 16))
label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=5, columnspan=6, padx=5, pady=5)

button1 = tk.Button(root, text="Enter", width=12, height=2, command=lambda: EnterAll())
button1.grid(row=1, column=12, columnspan=4, padx=5, pady=5)

label2 = tk.Label(root, text = "Enter b", font=('Times', 16))
label2.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=5, columnspan=6, padx=5, pady=5)

label3 = tk.Label(root, text = "Enter c", font=('Times', 16))
label3.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

entry3 = tk.Entry(root, width=40)
entry3.grid(row=2, column=5, columnspan=6, padx=5, pady=5)


labelx1_x2=tk.Label(root, text="", font=('Times', 16))
labelx1_x2.grid(row=5, column=0, columnspan=5, padx=5, pady=5)

labelx1x2=tk.Label(root, text="", font=('Times', 16))
labelx1x2.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

button4 = tk.Button(root, text="Count", width=12, height=2, command=lambda: CountAll(a, b, c))
button4.grid(row=4, column=12, columnspan=4, padx=5, pady=5)

labelx12x22 = tk.Label(root, text="", font=('Times', 16))
labelx12x22.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

labelPosOrNeg = tk.Label(root, text="", font=('Times', 16))
labelPosOrNeg.grid(row=8, column=1, columnspan=4, padx=5, pady=5)

labelNumPosOrNeg = tk.Label(root, text=znak, font=('Times', 16))
labelNumPosOrNeg.grid(row=9, column=1, columnspan=4, padx=5, pady=5)

root.mainloop()