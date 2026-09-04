operator  = input("enter the operation +,-,*,/ : ")

number1 = float(input("enter the number"))

number2 = float(input("enrter the number"))

if operator == "+":
    result = number1 + number2 
    print(result)

elif operator == "-":
    result = number1 - number2 
    print(round(result,3))

elif operator == "*":
    result = number1 * number2
    print(round(result,3))

elif operator == "/":
    result = number1 / number2 
    print(round(result,3))

else :
    print(" the",operator,"is not valid")






