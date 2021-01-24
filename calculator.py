import tkinter as tk
from functools import partial
global currentEq

window = tk.Tk()
window.title("Calculator")
# window.resizable(width=True, height=True)

window.columnconfigure(0, weight=10, minsize=50)
window.rowconfigure(0, weight=10, minsize=50)

frm_entry = tk.Frame(master=window)
lbl_ans = tk.Label(master=frm_entry, text="",bg='white',width=20,height = 4)

currentAns = 0
currentEq = ''

def update(x):
    global currentEq
    currentEq = str(currentEq) + x
    lbl_ans["text"] = currentEq

def delete():
    global currentEq
    currentEq =currentEq[:(len(currentEq)-1)]
    lbl_ans["text"] = currentEq

def evaluate():
    global currentEq
    try:
        currentEq = eval(currentEq)
        lbl_ans["text"] = str(currentEq)
    except SyntaxError:
        pass
    except ZeroDivisionError:
        lbl_ans["text"] = "Zero Division Error!"
        currentEq = ''

def clear():
    global currentEq
    currentEq = ''
    lbl_ans["text"] = currentEq

# region buttons
btn1 = tk.Button(master=frm_entry,text='1', command=partial(update,"1"), bg='white',fg='black', width=5,height=2)
btn2 = tk.Button(master=frm_entry,text='2', command=partial(update,"2"), bg='white',fg='black', width=5,height=2)
btn3 = tk.Button(master=frm_entry,text='3', command=partial(update,"3"), bg='white',fg='black', width=5,height=2)
btn4 = tk.Button(master=frm_entry,text='4', command=partial(update,"4"), bg='white',fg='black', width=5,height=2)
btn5 = tk.Button(master=frm_entry,text='5', command=partial(update,"5"), bg='white',fg='black', width=5,height=2)
btn6 = tk.Button(master=frm_entry,text='6', command=partial(update,"6"), bg='white',fg='black', width=5,height=2)
btn7 = tk.Button(master=frm_entry,text='7', command=partial(update,"7"), bg='white',fg='black', width=5,height=2)
btn8 = tk.Button(master=frm_entry,text='8', command=partial(update,"8"), bg='white',fg='black', width=5,height=2)
btn9 = tk.Button(master=frm_entry,text='9', command=partial(update,"9"), bg='white',fg='black', width=5,height=2)
btn0 = tk.Button(master=frm_entry,text='0', command=partial(update,"0"), bg='white',fg='black', width=5,height=2)

btnPlus = tk.Button(master=frm_entry,text='+', command=partial(update,"+"), width=5,height=2)
btnMin = tk.Button(master=frm_entry,text='-', command=partial(update,"-"), width=5,height=2)
btnMult = tk.Button(master=frm_entry,text='x', command=partial(update,"*"), width=5,height=2)
btnDiv = tk.Button(master=frm_entry,text='/', command=partial(update,"/"), width=5,height=2)
btnEq = tk.Button(master=frm_entry,text='=', command=evaluate, bg='red',fg='white', width=5,height=2)
btnCLR = tk.Button(master=frm_entry,text='CLR', command=clear, bg='red',fg='white', width=5,height=2)

# endregion

frm_entry.grid(row=0, column=0)

# region buttonsGrid
btn1.grid(row=1,column=0, sticky="nsew")
btn2.grid(row=1,column=1, sticky="nsew")
btn3.grid(row=1,column=2, sticky="nsew")
btn4.grid(row=2,column=0, sticky="nsew")
btn5.grid(row=2,column=1, sticky="nsew")
btn6.grid(row=2,column=2, sticky="nsew")
btn7.grid(row=3,column=0, sticky="nsew")
btn8.grid(row=3,column=1, sticky="nsew")
btn9.grid(row=3,column=2, sticky="nsew")
btn0.grid(row=4,column=1, sticky="nsew")

btnPlus.grid(row=1,column=3, sticky="nsew")
btnMin.grid(row=2,column=3, sticky="nsew")
btnMult.grid(row=3,column=3, sticky="nsew")
btnDiv.grid(row=4,column=3, sticky="nsew")
btnEq.grid(row=4,column=2, sticky="nsew")
btnCLR.grid(row=4,column=0, sticky="nsew")


# endregion

# region keyBinds
window.bind("1",lambda x: update("1"))
window.bind("2",lambda x: update("2"))
window.bind("3",lambda x: update("3"))
window.bind("4",lambda x: update("4"))
window.bind("5",lambda x: update("5"))
window.bind("6",lambda x: update("6"))
window.bind("7",lambda x: update("7"))
window.bind("8",lambda x: update("8"))
window.bind("9",lambda x: update("9"))
window.bind("0",lambda x: update("0"))

window.bind("+",lambda x: update("+"))
window.bind("-",lambda x: update("-"))
window.bind("*",lambda x: update("*"))
window.bind("/",lambda x: update("/"))
window.bind("<Return>", evaluate)
window.bind("<BackSpace>",delete)
# endregion


lbl_ans.grid(row=0, column=0, sticky="nsew",columnspan=4)

window.mainloop()