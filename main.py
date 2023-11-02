import tkinter as tk

root = tk.Tk()
root.title("Projekt na OOPa")
root.geometry("560x630")

a = 0
b = 0
c = 0

def PrzyjmijA():
    a = entry1.get()
    print(a)

def PrzyjmijB():
    b = entry2.get()
    print(b)

def PrzyjmijC():
    c = entry3.get()
    print(c)

def delta(a, b, c):
    global OblDelta
    OblDelta = (b*b)-4*a*c

def x1orazx2(a, b, c):
    global x1addx2
    global x1multiplyx2
    x1addx2 = (-1 * b) / a
    x1multiplyx2 = c / a

def sumaKwadratów(a, b, c):
    global kwadra
    kwadra = ((b*b) / (a*a)) - ((2 * c) / a)

def znaki():
    if x1multiplyx2 < 0:
        print("Liczby x1, x2 mają różne znaki")
    elif x1addx2 > 0:
        print("Liczby x1, x2 są dodatnie")
    else:
        print("Liczby są ujemne")

def update():
    pass

label1= tk.Label(root, text = "Wprowadź a", font=('Times', 16))
label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=5, columnspan=6, padx=5, pady=5)

button1 = tk.Button(root, text="Wprowadz", width=12, height=2, command=lambda: PrzyjmijA())
button1.grid(row=0, column=13, columnspan=4, padx=5, pady=5)

label2 = tk.Label(root, text = "Wprowadź b", font=('Times', 16))
label2.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=5, columnspan=6, padx=5, pady=5)

button2 = tk.Button(root, text="Wprowadz", width=12, height=2, command=lambda: PrzyjmijB())
button2.grid(row=1, column=13, columnspan=4, padx=5, pady=5)

label3 = tk.Label(root, text = "Wprowadź c", font=('Times', 16))
label3.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

entry3 = tk.Entry(root, width=40)
entry3.grid(row=2, column=5, columnspan=6, padx=5, pady=5)

button3 = tk.Button(root, text="Wprowadz", width=12, height=2, command=lambda: PrzyjmijC())
button3.grid(row=2, column=13, columnspan=4, padx=5, pady=5)



root.mainloop()