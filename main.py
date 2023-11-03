import tkinter as tk

root = tk.Tk()
root.title("Projekt na OOPa")
root.geometry("820x630")

x1addx2 = 0
x1multiplyx2 = 0
kwadra = 0
znak = ""

def PrzyjmijA():
    global a
    a = entry1.get()
    a = int(a)
    print(a)

def PrzyjmijB():
    global b
    b = entry2.get()
    b = int(b)
    print(b)

def PrzyjmijC():
    global c
    c = entry3.get()
    c = int(c)
    print(c)

def delta(a, b, c):
    global OblDelta
    OblDelta = (b*b)-4*a*c

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
    elif x1addx2 > 0:
        znak = "Numbers are positive"
        print("Numbers are positive")
    else:
        znak = "Numbers are negative"
        print("Numbers are negative")
    updateLabel5()

def updateLabel1and2():
   label1.config(text=("x1 + x2 = ", x1addx2))
   label2.config(text=("x1 * x2 = ", x1multiplyx2))
   root.after(100, updateLabel1and2)

def updateLabel3():
   label3.config(text=("x1^2 + x2^2 = ", kwadra))
   root.after(100, updateLabel3)

def updateLabel5():
   label5.config(text=znak)
   root.after(100, updateLabel5)

label1= tk.Label(root, text = "Enter a", font=('Times', 16))
label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=5, columnspan=6, padx=5, pady=5)

button1 = tk.Button(root, text="Enter", width=12, height=2, command=lambda: PrzyjmijA())
button1.grid(row=0, column=12, columnspan=4, padx=5, pady=5)

label2 = tk.Label(root, text = "Enter b", font=('Times', 16))
label2.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=5, columnspan=6, padx=5, pady=5)

button2 = tk.Button(root, text="Enter", width=12, height=2, command=lambda: PrzyjmijB())
button2.grid(row=1, column=12, columnspan=4, padx=5, pady=5)

label3 = tk.Label(root, text = "Enter c", font=('Times', 16))
label3.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

entry3 = tk.Entry(root, width=40)
entry3.grid(row=2, column=5, columnspan=6, padx=5, pady=5)

button3 = tk.Button(root, text="Enter", width=12, height=2, command=lambda: PrzyjmijC())
button3.grid(row=2, column=12, columnspan=4, padx=5, pady=5)

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

label4 = tk.Label(root, text="Are the numbers positive or negative", font=('Times', 16))
label4.grid(row=6, column=1, columnspan=4, padx=5, pady=5)

label5 = tk.Label(root, text=znak, font=('Times', 16))
label5.grid(row=7, column=1, columnspan=4, padx=5, pady=5)

button6 = tk.Button(root, text="Count", width=12, height=2, command=lambda: znaki())
button6.grid(row=7, column=12, columnspan=4, padx=5, pady=5)

root.mainloop()