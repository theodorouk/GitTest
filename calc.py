import tkinter as tk

class Calculator(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.pack()
    self.operators = []
    self.numbers = []
    self.current_number = None
    self.current_operator = None

    self.operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y,
                       '/': lambda x, y: x / y}

    # Create the display label
    self.display = tk.Label(self, text="0", font=("Helvetica", 32), bd=5, relief=tk.SUNKEN)
    self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    self.last_press_was_number = False
    # Create the buttons frame
    self.buttons_frame = tk.Frame(self)
    self.buttons_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    # Create the buttons
    self.create_buttons()

  def create_buttons(self):
    # Create the digits buttons
    for i in range(10):
      button = tk.Button(self.buttons_frame, text=str(i), width=5, command=lambda i=i: self.add_digit(i))
      button.grid(row=i // 3, column=i % 3)

    # Create the operator buttons
    operators = [('+', self.add), ('-', self.subtract), ('*', self.multiply), ('/', self.divide)]
    for i, (text, command) in enumerate(operators):
      button = tk.Button(self.buttons_frame, text=text, width=5, command=command)
      button.grid(row=i + 4, column=3)

    # Create the equal button
    equal_button = tk.Button(self.buttons_frame, text='=', width=5, command=self.equal)
    equal_button.grid(row=7, column=3)

    reset_button = tk.Button(self.buttons_frame, text='C', width=5, command=self.reset)
    reset_button.grid(row=4, column=0)

  def add_digit(self, digit):
    if self.current_operator is None:
      current_text = self.display['text']
      if current_text == '0':
        current_text = ''
      self.display['text'] = current_text + str(digit)
      self.last_press_was_number = True
    else:
      self.display['text'] = str(digit)

  def add(self):
    self.operate('+')

  def subtract(self):
    self.operate('-')

  def multiply(self):
    self.operate('*')

  def divide(self):
    self.operate('/')

  def operate(self, operator):
    self.current_number = float(self.display['text'])
    self.current_operator = operator


  def store_current_number(self):
    self.numbers.append(float(self.display['text']))
    self.display['text'] = '0'

  def equal(self):
    if self.current_operator is not None:
      result = self.operations[self.current_operator](self.current_number, float(self.display['text']))
      self.display['text'] = str(result)
      self.current_number = None
      self.current_operator = None

  def reset(self):
    self.display['text'] = '0'
    self.operators = []
    self.numbers = []

root = tk.Tk()
root.title("Calculator")
app = Calculator(root)
root.mainloop()
