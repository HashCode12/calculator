# main file for the calculator


def main():
    num1 = int(numbers())
    num2 = int(numbers())
    calculation = operation()
    output = calculate(calculation , num1 , num2)
    print(output)


def numbers():
    while True:
        num = input("Number: ")

        if num.isdigit():
            break
        else:
            print("Enter Number again")
    return num

def operation():
    while True:
        operations = input("Enter Operation: ")

        if operations == "+" :
            break
        elif operations == "-" :
            break
        elif operations == "*" :
            break
        elif operations == "/":
            break
        else:
            print("Please enter valid operation...")
        
    return operations

def calculate(n , num1 , num2):
    if n == "+":
        ans = num1 + num2
    elif n == "-":
        ans = num1 - num2
    elif n == "*":
        ans = num1 * num2
    else:
        ans = num1/num2
    return ans

main()