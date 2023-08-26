import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
frame = tk.Frame(master=window,padx=10,bg="#669999")
frame.pack()
entry = tk.Entry(master=frame, borderwidth=20,width=27,font=("Algerian",20,'bold'),bd=30,fg="white",bg="#1a1a1a",)
entry.grid(row=0, column=0, columnspan=4, ipady=25, pady=25)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

button_1 = tk.Button(master=frame, text='1',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(4))
button_4.grid(row=1, column=3, pady=2)
button_5 = tk.Button(master=frame, text='5',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(5))
button_5.grid(row=2, column=0, pady=2)
button_6 = tk.Button(master=frame, text='6',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(6))
button_6.grid(row=2, column=1, pady=2)
button_7 = tk.Button(master=frame, text='7',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(7))
button_7.grid(row=2, column=2, pady=2)
button_8 = tk.Button(master=frame, text='8',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(8))
button_8.grid(row=2, column=3, pady=2)
button_9 = tk.Button(master=frame, text='9',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(9))
button_9.grid(row=3, column=0, pady=2)
button_0 = tk.Button(master=frame, text='0',width=5,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#a6a6a6", command=lambda: myclick(0))
button_0.grid(row=3, column=1, pady=2)
button_add = tk.Button(master=frame, text="+",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('+'))
button_add.grid(row=3, column=2, pady=2)

button_subtract = tk.Button(
    master=frame, text="-",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('-'))
button_subtract.grid(row=3, column=3, pady=2)

button_multiply = tk.Button(
    master=frame, text="x",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('*'))
button_multiply.grid(row=5, column=0, pady=2)

button_div = tk.Button(master=frame, text="÷",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('/'))
button_div.grid(row=5, column=1, pady=2)

button_square1 = tk.Button(master=frame, text="a^b",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('**'))
button_square1.grid(row=5, column=2, columnspan=1, pady=2)

button_square1 = tk.Button(master=frame, text="√",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('**(1/2)'))
button_square1.grid(row=5, column=3, columnspan=1, pady=2)

button_square1 = tk.Button(master=frame, text="C to F",width=5,height=2,font=("Algerian",20,'bold'),bd=10,fg="yellow",bg="#000000", command=lambda: myclick('*(9/5)+32'))
button_square1.grid(row=6, column=3, columnspan=1, pady=2)

button_clear = tk.Button(master=frame, text="clear",width=5,height=2,font=("arial",20,'bold'),bd=10,fg="yellow",bg="blue", command=clear)
button_clear.grid(row=6, column=2, columnspan=1,rowspan=2, pady=2)

button_equal = tk.Button(master=frame, text="=",width=13,height=2,font=("arial",20,'bold'),bd=10,fg="#fff",bg="#ffad33", command=equal)
button_equal.grid(row=6, column=0, columnspan=2,pady=2)

window.mainloop()
