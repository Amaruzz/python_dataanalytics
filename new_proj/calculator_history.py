#Start the program
#Define the name of the history file
history_file = "calculator_history.txt"

def show_history():
   file=open(history_file,"r")
   lines=file.readlines()
   if len(lines)==0:
      print("No history found.")
    else:
       for line in reversed(lines):
            print(line.strip())
#loop forever(While=True)
#a) Ask user to calculate(like 8+5) or a command (history,exit,clear)
# b) If user types "exit":
# i)Print thank you message
# ii) Break the loop
#c) If user types "history":
# i) Open the history file in read mode
# ii)I file exist and not empty,read and print the file
#iii) If file doesnt exist or empty,print no history message
#d) If user types "clear":
# i) Open the history file and overwrite it with nothing(empty it)
# ii) Print history cleared message
#e) Else(assume user entered calculations):
#i) Parse the input to get the numbers and the operator(You can split the input by spac, eg:-"8 +5")
#ii) If input is not valid(print invalid input message and continue to next iteration of loop)
#iii) Perform the calculation based on if/elif:
# + : addition
# - : subtraction
# * : multiplication
# / : division
#iv) Print the result
#v) Append the calculation and result to the history file