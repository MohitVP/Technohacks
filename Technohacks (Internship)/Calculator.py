import tkinter as tk

def update_display(value):
    current_value = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_value + str(value))

def delete():
    current_value = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_value[:-1])

def clear():
    entry_display.delete(0, tk.END)

def calculate():
    expression = entry_display.get()
    try:
        result = eval(expression)
        lbl_result.config(text="Result: " + str(result))
    except:
        lbl_result.config(text="Invalid expression.")

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")

# Create the display field
entry_display = tk.Entry(window, width=25, font=("Arial", 20))
entry_display.grid(row=0, column=0, columnspan=4, pady=20)

# Create number buttons
btn_numbers = []
for i in range(9):
    btn = tk.Button(window, text=str(i+1), width=8, height=4, font=("Arial", 14), command=lambda i=i: update_display(i+1))
    btn.grid(row=1 + i // 3, column=i % 3, padx=5, pady=5)
    btn_numbers.append(btn)

# Create operation buttons
btn_add = tk.Button(window, text="+", width=8, height=4, font=("Arial", 14), command=lambda: update_display("+"))
btn_add.grid(row=4, column=0, padx=5, pady=5)

btn_subtract = tk.Button(window, text="-", width=8, height=4, font=("Arial", 14), command=lambda: update_display("-"))
btn_subtract.grid(row=4, column=1, padx=5, pady=5)

btn_multiply = tk.Button(window, text="*", width=8, height=4, font=("Arial", 14), command=lambda: update_display("*"))
btn_multiply.grid(row=4, column=2, padx=5, pady=5)

btn_divide = tk.Button(window, text="/", width=8, height=4, font=("Arial", 14), command=lambda: update_display("/"))
btn_divide.grid(row=4, column=3, padx=5, pady=5)

# Create utility buttons
btn_delete = tk.Button(window, text="Del", width=8, height=4, font=("Arial", 14), command=delete, bg="#ffcccc")
btn_delete.grid(row=1, column=3, padx=5, pady=5)

btn_clear = tk.Button(window, text="AC", width=8, height=4, font=("Arial", 14), command=clear, bg="#ffcccc")
btn_clear.grid(row=2, column=3, padx=5, pady=5)

# Create calculate button
btn_calculate = tk.Button(window, text="=", width=8, height=4, font=("Arial", 14), command=calculate)
btn_calculate.grid(row=3, column=3, padx=5, pady=5)

# Create a label to display the result
lbl_result = tk.Label(window, text="Result:", font=("Arial", 16))
lbl_result.grid(row=6, column=0, columnspan=4, pady=20)

# Start the main loop
window.mainloop()
