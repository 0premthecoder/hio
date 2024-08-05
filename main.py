import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button_text in button_list:
            if button_text == "=":
                button = tk.Button(master, text=button_text, width=9, height=2, command=self.equal)
                button.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
                col += 2
            else:
                button = tk.Button(master, text=button_text, width=5, height=2, command=lambda x=button_text: self.button_click(x))
                button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + button)

    def equal(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
