import tkinter as tk

from tkinter import *

top = Tk()

top.geometry("500x500")
answer = Text(width=40, height=3)
answer.place(x=100, y=100)


def show(x):
    if x == "=":
        final_answer = eval(answer.get(1.0, "end-1c"))
        answer.insert(tk.INSERT, x)
        answer.insert(tk.INSERT, final_answer)
    else:
        answer.insert(tk.INSERT, x)


B1 = Button(top, text="1", width=4, height=2, command=lambda: show("1"))
B1.place(x=110, y=155)

B2 = Button(top, text="2", width=4, height=2, command=lambda: show("2"))
B2.place(x=160, y=155)

B3 = Button(top, text="3", width=4, height=2, command=lambda: show("3"))
B3.place(x=210, y=155)

B4 = Button(top, text="4", width=4, height=2, command=lambda: show("4"))
B4.place(x=260, y=155)

B5 = Button(top, text="5", width=4, height=2, command=lambda: show("5"))
B5.place(x=310, y=155)

B6 = Button(top, text="6", width=4, height=2, command=lambda: show("6"))
B6.place(x=360, y=155)

B7 = Button(top, text="7", width=4, height=2, command=lambda: show("7"))
B7.place(x=160, y=205)

B8 = Button(top, text="8", width=4, height=2, command=lambda: show("8"))
B8.place(x=210, y=205)

B9 = Button(top, text="9", width=4, height=2, command=lambda: show("9"))
B9.place(x=260, y=205)

B10 = Button(top, text="0", width=4, height=2, command=lambda: show("0"))
B10.place(x=310, y=205)

B11 = Button(top, text="+", width=4, height=2, command=lambda: show("+"))
B11.place(x=160, y=255)

B12 = Button(top, text="-", width=4, height=2, command=lambda: show("-"))
B12.place(x=210, y=255)

B13 = Button(top, text="/", width=4, height=2, command=lambda: show("/"))
B13.place(x=260, y=255)

B14 = Button(top, text="=", width=4, height=2, command=lambda: show("="))
B14.place(x=310, y=305)

B15 = Button(top, text="*", width=4, height=2, command=lambda: show("*"))
B15.place(x=310, y=255)

B16 = Button(top, text="c", width=4, height=2, command=lambda: answer.delete(1.0, END))
B16.place(x=160, y=305)
top.mainloop()
