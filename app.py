# Import required modules
from tkinter import *
import tkinter.font as font

# Creating the main window
root = Tk()
 
# Assigning it the desired geometry
root.geometry("400x430")
 
# Assigning the name of our window
root.title("Calculator")
 
root.resizable(0, 0)
 
inp = StringVar()
myFont = font.Font(size=20)
 
screen = Entry(root, text=inp, width=35,
               justify='right', font=(12), bd=8)
 
# We will use a grid like structure
screen.grid(row=0, columnspan=4, padx=15,
            pady=15, ipady=5)
 
# Key matrix contains all the required the keys
key_matrix = [["/", u"\u221A", "<-", "c"],
              ["1", "2", "3", "*"],
              ["4", "5", "6", "+"],
              ["7", "8", "9", "-"],
              ["!", 0, ".", "="]]
 
# Creating a dictionary for the buttons
btn_dict = {}
 
# Variable to store our results
ans_to_print = 0
 
# Defining the function for calculation
def Calculate(event):
   
    # getting the name of the button clicked
    button = event.widget.cget("text")
 
    # Referring the global values
    global key_matrix, inp, ans_to_print
 
    try:
        # Event containing a sqrt operation
        if button == u"\u221A":
            ans = float(inp.get())**(0.5)
            ans_to_print = str(ans)
            inp.set(str(ans))
 
        elif button == "c": # Clear Button
            inp.set("")
 
        elif button == "!": # Factorial
            def fact(n): return 1 if n == 0 else n*fact(n-1)
            inp.set(str(fact(int(inp.get()))))
 
        elif button == "<-": # Backspace
            inp.set(inp.get()[:len(inp.get())-1])
 
        elif button == "=": # Showing The Results
            # Calculating the mathematical exp. using eval
            ans_to_print = str(eval(inp.get()))
            inp.set(ans_to_print)
 
        else:
            # Displaying the digit pressed on screen
            inp.set(inp.get()+str(button))
 
    except:
        # In case invalid syntax given in expression
        inp.set("Wrong Operation")
  
# Number of rows containing buttons
for i in range(len(key_matrix)): 
    # Number of columns 
    for j in range(len(key_matrix[i])): 
 
        # Creating and Adding the buttons to dictionary
        btn_dict["btn_"+str(key_matrix[i][j])] = Button(
          root, bd=1, text=str(key_matrix[i][j]), font=myFont)
         
        # Positioning buttons
        btn_dict["btn_"+str(key_matrix[i][j])].grid(
          row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
         
        # Assigning an action to the buttons
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate)
 
# Running the main loop
root.mainloop()