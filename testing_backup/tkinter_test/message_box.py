import tkinter as tk
import tkinter.messagebox as ms

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

def onclick(k):
    if k == 0:
        ms.showinfo(title='Hi', message='hello!')
    elif k == 1:
        ms.showwarning(title='Hi', message='hello?')
    elif k == 2:
        ms.showerror(title='Hi', message='hello??')
    elif k == 3:
        ms.askquestion(title='Hi', message='hello???')
    elif k == 4:
        ms.askyesno(title='Hi', message='hello!?')
    elif k == 5:
        ms.askokcancel(title='Hi', message='hello...')

btn_list = list()
for i in range(6):
    btn = tk.Button(window, text="Button" + str(i + 1), command=lambda x=i: onclick(x))
    btn.pack()

window.mainloop()