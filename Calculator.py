import tkinter as tk 
from tkinter import ttk 


root=tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#b4b1b1")

# Grid Configuration
for i in range(6):
    root.grid_rowconfigure(i,weight=1)

for i in range(4):
    root.grid_columnconfigure(i,weight=1)

display=tk.Text(root,font=("Arial",28),bd=2,relief=tk.RIDGE,height=2)
display.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky="nsew")
# Right Alignment
display.tag_configure("right",justify="right")


def btn_click(value):
    display.insert(tk.END,value)

def clear_display():
    display.delete("1.0",tk.END)

def backspace():
    content=display.get("1.0",tk.END)
    if len(content)>1:
        content=content[:-2]
        display.delete("1.0",tk.END)
        display.insert("1.0",content)
        display.tag_add("right","1.0","end")

def equal():
    try:
        expression=display.get("1.0",tk.END).strip()
        result=eval(expression)
        display.delete("1.0",tk.END)
        display.insert(tk.END,expression+"\n")
        display.insert(tk.END,str(result))
        display.tag_add("right","1.0","end")
    except Exception as e:
        display.delete("1.0",tk.END)
        display.insert(tk.END,"\nError")

# Row 1
btn_clear = tk.Button(root, text="AC", font=("Arial", 25), command=clear_display)
btn_clear.grid(row=1, column=0, sticky="nsew")

btn_mod = tk.Button(root, text="%", font=("Arial", 25), command=lambda: btn_click("%"))
btn_mod.grid(row=1, column=1, sticky="nsew")

btn_bcks = tk.Button(root, text="<-", font=("Arial", 25), command=backspace)
btn_bcks.grid(row=1, column=2, sticky="nsew")

btn_div = tk.Button(root, text="/", font=("Arial", 25), command=lambda: btn_click("/"))
btn_div.grid(row=1, column=3, sticky="nsew")

# Row 2
btn_seven = tk.Button(root, text="7", font=("Arial", 25), command=lambda: btn_click("7"))
btn_seven.grid(row=2, column=0, sticky="nsew")

btn_eight = tk.Button(root, text="8", font=("Arial", 25), command=lambda: btn_click("8"))
btn_eight.grid(row=2, column=1, sticky="nsew")

btn_nine = tk.Button(root, text="9", font=("Arial", 25), command=lambda: btn_click("9"))
btn_nine.grid(row=2, column=2, sticky="nsew")

btn_mul = tk.Button(root, text="*", font=("Arial", 25), command=lambda: btn_click("*"))
btn_mul.grid(row=2, column=3, sticky="nsew")

# Row 3
btn_four = tk.Button(root, text="4", font=("Arial", 25), command=lambda: btn_click("4"))
btn_four.grid(row=3, column=0, sticky="nsew")

btn_five = tk.Button(root, text="5", font=("Arial", 25), command=lambda: btn_click("5"))
btn_five.grid(row=3, column=1, sticky="nsew")

btn_six = tk.Button(root, text="6", font=("Arial", 25), command=lambda: btn_click("6"))
btn_six.grid(row=3, column=2, sticky="nsew")

btn_sub = tk.Button(root, text="-", font=("Arial", 25), command=lambda: btn_click("-"))
btn_sub.grid(row=3, column=3, sticky="nsew")

# Row 4
btn_one = tk.Button(root, text="1", font=("Arial", 25), command=lambda: btn_click("1"))
btn_one.grid(row=4, column=0, sticky="nsew")

btn_two = tk.Button(root, text="2", font=("Arial", 25), command=lambda: btn_click("2"))
btn_two.grid(row=4, column=1, sticky="nsew")

btn_three = tk.Button(root, text="3", font=("Arial", 25), command=lambda: btn_click("3"))
btn_three.grid(row=4, column=2, sticky="nsew")

btn_add = tk.Button(root, text="+", font=("Arial", 25), command=lambda: btn_click("+"))
btn_add.grid(row=4, column=3, sticky="nsew")

# Row 5
btn_double_zero = tk.Button(root, text="00", font=("Arial", 25), command=lambda: btn_click("00"))
btn_double_zero.grid(row=5, column=0, sticky="nsew")

btn_zero = tk.Button(root, text="0", font=("Arial", 25), command=lambda: btn_click("0"))
btn_zero.grid(row=5, column=1, sticky="nsew")

btn_dot = tk.Button(root, text=".", font=("Arial", 25), command=lambda: btn_click("."))
btn_dot.grid(row=5, column=2, sticky="nsew")

btn_equal = tk.Button(root, text="=", font=("Arial", 25), command=equal)
btn_equal.grid(row=5, column=3, sticky="nsew")


# run the application
root.mainloop()