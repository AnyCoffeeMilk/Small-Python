import tkinter as tk

window  = tk.Tk()
window.title("Window")
window.geometry("500x500")

label_a = tk.Label(window, text="Hello World!", bg="white", font=('Arial', 12), width=15, height=1)
label_a.pack()

label_b = tk.Label(window, text="Hello World!", bg="red", font=('Arial', 12), width=15, height=1)
label_b.pack()

label_c = tk.Label(window, text="Hello World!", bg="blue", font=('Arial', 12), width=15, height=1)
label_c.place(x=10, y=0)

label_d = tk.Label(window, text="Hello World!", bg="green", fg="yellow" , font=('Arial', 12), width=15, height=1)
label_d.place(x=350, y=0)

window.mainloop()