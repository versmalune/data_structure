from stack import Stack

def infix_to_postfix(infixexp):
    s = Stack()
    ret = []
    prec = {}
    prec['/'] = 3
    prec['*'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    token_list = infixexp.split()

    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789'
            ret.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                ret.append(top_token)
                top_token = s.pop()
        else:
            while (not s.is_empty()) and (prec[s.peek()] >= prec[token]):
                ret.append(s.pop())
            s.push(token)
            #print(s.peek())

    while not s.is_empty():
        opToken = s.pop()
        ret.append(opToken)
    return " ".join(ret)


# evaluating postfix expression
# push all numbers to the stack until operator -> pop 2 numbers from stack and calculate with the operator
# -> push the result to the stack -> repeat
def eval_postfix(str):
    stack = Stack()
    token_list2 = str.split()
    
    for token in token_list2:
        if token in ("+", "-", "*", "/"):
            a, b = stack.pop(), stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(b - a)
            elif token == '*':
                stack.push(b * a)
            elif token == '/':
                stack.push(b / a)
        else:
            stack.push(int(token))
    return stack.pop()


def expr_test(infix):
    postfix = infix_to_postfix(infix)
    result = eval_postfix(postfix)
    print("'%s' => '%s' = %f" % (infix, postfix, result))


if __name__ == '__main__':
    expr_test("4 + 3 - 2")
    expr_test("4 + 3 - 4 / 2")
    expr_test("1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 3 + 5 * 2 ) * ( 3 - 1 )")


    
# '4 + 3 - 2' = > '4 3 + 2 -' = 5.000000
# '4 + 3 - 4 / 2' = > '4 3 + 4 2 / -' = 5.000000
# '1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 3 * + 4 2 4 5 2 + - / * -' = 9.666667
# '( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 + 3 * 4 2 4 5 2 + - / * -' = 11.666667
