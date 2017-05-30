from stack import Stack
from tokenizer import tokenize

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def to_postfix(infix):
    tezine = {}
    
    tezine["^"] = 4
    tezine["*"] = 3
    tezine["/"] = 3
    tezine["+"] = 2
    tezine["-"] = 2
    tezine["("] = 1
    tezine[")"] = 1
          
    postfix = []
    operators = Stack()

    for token in infix:
        if is_number(token):
            postfix.append(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            top = operators.pop()
            while top != '(':
                postfix.append(top)
                top = operators.pop()
        else:
            while not operators.is_empty() and \
                  tezine[operators.top()] >= tezine[token]:
                postfix.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        postfix.append(operators.pop())
    return " ".join(postfix)


def postfixEval(postfixExpr):
    operands = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if is_number(token):
            operands.push(float(token))
        else:
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = doMath(token, operand1, operand2)
            operands.push(result)
    return operands.pop()


def doMath(op, op1, op2):
    try:
        
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        elif op == "^":
            return op1 ** op2
        else:
            return op1 - op2

    except ZeroDivisionError:
        print "Con't divide by zero!"
        validate = False

  
def infix_validation(infix):
    brackets = 0
    operands = 0
    operators = 0
    caracters = True
    validate = True
    
    for token in infix:
        if is_number(token):
            operands += 1
        elif token == "(":
            brackets += 1
        elif token == ")":
            brackets -= 1
        elif token == "^" or token == "+" or token == "-" or token == "*" or token == "/":
            operators += 1
        elif token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            caracters = False
    
    if infix[0] == "^" or infix[0] == "+" or infix[0] == "-" or infix[0] == "*" or infix[0] == "/":
        print("Error! Expression mustn't start with operator!")
        validate = False
            
    for x, y in zip(infix, infix[1:]):
        if is_number(x) == True and is_number(y) == True:
            print("Error! Two operands with out an operator!")
            validate = False
    
    for x, y in zip(infix, infix[1:]):
        if (x == "^" or x == "+" or x == "-" or x == "*" or x == "/") & (y == "^" or y == "+" or y == "-" or y == "*" or y == "/"):
            print("Error Two operators with out an operand!")
            validate = False
    
    for x, y in zip(infix, infix[1:]):
        if (x == "(") and (y == ")"):
            print("Error No expression inside the brackets!")
            validate = False    
    
    for x, y in zip(infix, infix[1:]):
        if (x == "(") and not (is_number(y) == True or y == "("):
            print("Error! After open brackets must follow an operand or another open brackets!")
            validate = False  
    
    for x, y in zip(infix, infix[1:]):
        if (x == ")") and not (y == "^" or y == "+" or y == "-" or y == "*" or y == "/" or y == ")"):
            print("Error! After closing brackets must follow an operator or another closing brackets!")
            validate = False  
            
    for x, y in zip(infix, infix[1:]):
        if (y == "(") and not (x == "^" or x == "+" or x == "-" or x == "*" or x == "/" or x == "("):
            print("Error! Before opening brackets must go an operator or another opening brackets!")
            validate = False 
    
    for x, y in zip(infix, infix[1:]):
        if (y == ")") and not (is_number(x) == True or x == ")"):
            print("Error! Before closing brackets must go an operand or another closing brackets!")
            validate = False 
            
    if len(infix) <= 1:
        print("Error! You don't have enough operators in expression!")
        validate = False
        
    if brackets != 0:
        print("Error! The number of opeing and closing brackets doesn't match!")
        validate = False
        
    if caracters == False:
        print("Error! Bad characters usage!")
        validate = False
    
    if operators+1 != operands:
        print("Error! The combination of operands and operators is unvalidate!")
        validate = False
        
    if operators >= operands:
        print("Error! You have more operators and operands!")
        validate = False
        
    if operators+1 < operands:
        print("Error! You have more operands and operators!")
        validate = False
    
    return validate


if __name__ == '__main__':
    var = input("Please enter your expression: ")
    tokens = tokenize(var)
    validate = infix_validation(tokens)
    
    while validate != True:
        var = input("\nPlease try again: ")
        tokens = tokenize(var)
        validate = infix_validation(tokens)
        
    if validate == True:
        infix = " ".join(tokens)
        print("Infix: ", infix)
        postfix = to_postfix(tokens)
        print("Postfix: ", postfix)
        result = postfixEval(postfix)
        print("Result: ", result)