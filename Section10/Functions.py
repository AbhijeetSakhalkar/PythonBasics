# https://www.w3schools.com/python/python_functions.asp

def addTwoNumbers(x,y):
    return x + y

c = addTwoNumbers(3 ,4)
print(c)

def printMenu():
    print ("In print Menu")

printMenu()

##############################################
def func(name = 'abhijeet'):
    print("Name is "+ name)

func('rohan')
func('mohan')
func() # default parameter used