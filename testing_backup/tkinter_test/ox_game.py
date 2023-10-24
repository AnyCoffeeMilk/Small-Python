import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("500x500")

turn = tk.BooleanVar()
turn.set(True)
label = tk.Label(window, text="", width=15, height=1)
label.pack()

def a(b):
    return btn_list[b]['text']

def onclick(k):
    btn = btn_list[k]
    if btn['text'] == " ":
        if turn.get() == True:
            btn['text'] = "O"
            turn.set(False)
        else:
            btn['text'] = "X"
            turn.set(True)
    for i in range(3):
        if  (a(i) == a(i + 3) and a(i + 3) == a(i + 6) and a(i) != " ") or \
            (a(i * 3) == a(i * 3 + 1) and a(i * 3 + 1) == a(i * 3 + 2) and a(i * 3) != " ") or \
            (a(2) == a(4) and a(4) == a(6) and a(2) != " ") or \
            (a(0) == a(4) and a(4) == a(8) and a(0) != " "):
            
            label['text'] = "You Win"
            for y in range(9):
                btn_list[y]['text'] = " "
            turn.set(True)

btn_list = list()
for y in range(3):
    for i in range(3):
        btn = tk.Button(window, text=" ", width=10, height=5, command=lambda p=i, q=y: onclick(p + q * 3))
        btn.place(x=100 + 100 * y, y=100 + 100 * i)
        btn_list.append(btn)

window.mainloop()