#exercise 6
x=0
def calculator(num1,num2,operator,x):
    if operator == "+":
        x=num1 + num2
    elif operator == "-":
        x=num1 - num2
    elif operator == "*":
        x=num1 * num2
    elif operator == "/":
        x=num1 / num2
    else:
        ValueError("Insert +,-,*,/")

    if format == "integer":
        print(int(x))
    elif format == "float":
        print(float(x))
    else:
        ValueError("Insert Integer or float!")

operator=input("Insert Your symbols of math :")
num1=int(input("Insert First Number :"))
num2=int(input("Insert Second Number :"))
format=input("Format :")
calculator(num1,num2,operator,x)
