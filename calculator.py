
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Error!Division by the zero."
    else:
        return x/y
num1=float(input("Enter the number1:"))
num2=float(input("Enter the number2:"))
print("Select the operation:")
print("1.Addition:")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
choice=input("Enter choice(1/2/3/4):")
if choice=="1":
    result=add(num1,num2)
elif choice=="2":
    result=sub(num1,num2)
elif choice=="3":
    result=multi(num1,num2)
elif choice=="4":
    result=div(num1,num2)
else:
    result="Invalid Input."
print("Result:",result)    
