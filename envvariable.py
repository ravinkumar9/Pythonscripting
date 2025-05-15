import os
import sys

#print(os.getenv("AWS_ACCESS_KEY_ID"))
#print(os.getenv("AWS_SECRET_KEY"))

#Output will be taken from the Operating system.

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2


#ensuring the correct no of arguments are provided.
if len(sys.argv) < 4:
    print("usage: envvariable.py <number 1> <operation> <number 2>")
    sys.exit(1)
else:
    print("value should not be no-numeric")

script_name=sys.argv[0]
num1=float(sys.argv[1])
operation=(sys.argv[2])
num2=float(sys.argv[3])

if operation == "add":
    print(add(num1,num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mul":
    print(mul(num1,num2))
else:
    print("accepted value is only add, sub and mod")

#note : if we give sys.argv[0]. When we give the input it will start treating the other args as input.
#for eg : if we put python environment.py 2 add 3 . First input it will consider as environment.py followed by 2 add 3.
