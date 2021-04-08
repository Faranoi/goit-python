result = None
operand = None
operator = None
wait_for_number = True
while True:
    result = input("Enter first digit: ")
    try:
        result = int(result)
    except ValueError or TypeError:
        print (f"{result} is not a digit")
    else:
        break
while True:
    operator = input ("Enter an operator: ")
    if operator not in ("+","-","/","*","="):
        print (f"{operator} is not correct")
        continue
    elif operator == "=":
        break
    operand = input ("Enter next digit: ")
    if operand == "=":
        break
    while True:
        try:
            operand = int(operand)
        except ValueError or TypeError:
            print (f"{operand} is not a digit")
            operand = input ("Enter next digit: ")
        else:
            operand = int(operand)
            break
    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        result /= operand
print (result)