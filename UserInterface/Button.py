import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("500x500")

counter = tk.IntVar()

label_text = tk.StringVar()
label_text.set("Counter: 0")
label = tk.Label(window, textvariable=label_text, width=15, height=1)
label.pack()

def onclick(increment):
    counter.set(counter.get() + increment)
    label_text.set("Counter: " + str(counter.get()))
    label['font'] = ('Arial', 15 + counter.get())

btn = tk.Button(window, text="Button", width=15, height=4, command=lambda:onclick(1))
btn.pack()

window.mainloop()