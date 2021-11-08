def add(n1, n2):
    answer = n1 + n2
    return answer

def subtract(n1, n2):
    answer = n1 - n2
    return answer

def multiply(n1, n2):
    answer = n1 * n2
    return n1 * n2

def divide(n1, n2):
    answer = n1 / n2
    return answer

operations = {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide
}

def calculator():
    process = True
    num1 = float(input("type the first number: "))

    while process == True:

        for symbol in operations.keys():
            print(symbol)

        op_selected = input("Please select an operation ")

        num2 = float(input("type the second number: "))

        math_op = operations[op_selected]
        answer= math_op(num1, num2)

        print(f"{num1} {op_selected} {num2} = {answer}")

        ending = input("Do you want to perform another operation? Y or N   ").lower()

        if ending == "n":
            process = False
            print("goodbye!")
        elif ending == "y":
            ending2 = input("Do you want to reset the calculator? Y or N   ").lower()
            if ending2 == "y":
                calculator()
            elif ending2 == "n":
                num1 = answer
                print(num1)
            
            
calculator()

