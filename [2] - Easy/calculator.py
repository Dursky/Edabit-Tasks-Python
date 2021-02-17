
def calculator(num1,operator,num2):
    if(operator == "+"):
        return num1 + num2
    if(operator == "-"):
        return num1 - num2
    if(operator == "*"):
        return num1 * num2
    if(operator == "/"):
        return num1 // num2

print(calculator(8,"*",8))