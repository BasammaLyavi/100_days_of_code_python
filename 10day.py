import art10

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multy(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
operations={
    '+':add,
    '-':sub,
    '*':multy,
    '/':divide
}
def calculator():
    print(art10.logo)
    should_accumulate=True
    num1=float(input("What is the First number?:"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick the symbol:")
        num2=float(input("What is the Second number?:"))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")

        choice=input(f"Type 'yes' to continue to calculate with {answer},or type 'no'\n")
        if choice=="yes":
            num1=answer
        else:
            should_accumulate="False"
            print(("\n"*20))
            calculator()

calculator()

