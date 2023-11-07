import tkinter as tk

root = tk.Tk()
root.title("Projekt na OOPa")
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
    print(a)

    global b
    b = entry2.get()
    b = int(b)
    print(b)

    global c
    c = entry3.get()
    c = int(c)
    print(c)

def delta(a, b, c):
    global OblDelta
    OblDelta = (b*b)-4*a*c
    updateLabel4()

def x1orazx2(a, b, c):
    global x1addx2
    global x1multiplyx2
    x1addx2 = (-1 * b) / a
    x1multiplyx2 = c / a
    updateLabel1and2()

def sumaKwadratów(a, b, c):
    global kwadra
    kwadra = ((b*b) / (a*a)) - ((2 * c) / a)
    updateLabel3()

def znaki():
    global znak
    if x1multiplyx2 < 0:
        znak = "Numbers x1, x2 have different signs"
        print("Numbers x1, x2 have different signs")
        updateLabel5()
    elif x1addx2 > 0:
        znak = "x1 and x2 are positive"
        print("Numbers are positive")
        updateLabel5()
    else:
        znak = "x1 and x2 are negative"
        print("Numbers are negative")
        updateLabel5()


def updateLabel1and2():
   label1.config(text=("x1 + x2 = ", x1addx2))
   label2.config(text=("x1 * x2 = ", x1multiplyx2))

def updateLabel3():
   label3.config(text=("x1^2 + x2^2 = ", kwadra))


def updateLabel4():
    label4.config(text=("Delta is equal to ", OblDelta))

def updateLabel5():
    label5.config(text=znak)


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

label1=tk.Label(root, text=("x1 + x2 = ", x1addx2), font=('Times', 16))
label1.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

label2=tk.Label(root, text=("x1 * x2 = ", x1multiplyx2), font=('Times', 16))
label2.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

button4 = tk.Button(root, text="Count", width=12, height=2, command=lambda: x1orazx2(a ,b, c))
button4.grid(row=4, column=12, columnspan=4, padx=5, pady=5)

label3 = tk.Label(root, text=("x1^2 + x2^2 = ", kwadra), font=('Times', 16))
label3.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

button5 = tk.Button(root, text="Count", width=12, height=2, command=lambda: sumaKwadratów(a ,b, c))
button5.grid(row=5, column=12, columnspan=4, padx=5, pady=5)


label4 = tk.Label(root, text=("Delta is equal to ", OblDelta),font=('Times', 16))
label4.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

button6 = tk.Button(root, text="Count", width=12, height=2, command=lambda: delta(a, b, c))
button6.grid(row=6, column=13, columnspan=4, padx=5, pady=5)

label6 = tk.Label(root, text="Are the numbers positive or negative", font=('Times', 16))
label6.grid(row=8, column=1, columnspan=4, padx=5, pady=5)

label5 = tk.Label(root, text=znak, font=('Times', 16))
label5.grid(row=9, column=1, columnspan=4, padx=5, pady=5)

button6 = tk.Button(root, text="Count", width=12, height=2, command=lambda: znaki())
button6.grid(row=9, column=12, columnspan=4, padx=5, pady=5)

root.mainloop()