def decorate(func):
    def wrapper(a,b):
       print("the addition to u r number are")
       func(a,b)
       print("Thankyou I hope u liked it")
    return wrapper

 

@decorate
def addition(a,b):
    print(f" Your total is{a+b}")

addition(12,67)