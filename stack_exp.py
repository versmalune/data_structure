"""
학번: 60171670
이름: 홍유진
"""

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
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789': #숫자일 떄
            ret.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                ret.append(top_token)
                top_token = s.pop()
        else: #연산자일 때
            while (not s.is_empty()) and (prec[s.peek()] >= prec[token]):
                ret.append(s.pop())
            s.push(token)
            #print(s.peek())

    while not s.is_empty():
        opToken = s.pop()
        ret.append(opToken)
    return " ".join(ret)


# postfix 계산하기
# 이미 postfix로 변환된 값을 계산만 하면 됨
# 연산자 입력될 때까지 계속 숫자를 stack에 push -> 연산자 하나 입력 -> stack에서 2개 pop -> 계산 -> 계산 결과값 다시 stack에 push -> 반복
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

# 실행 결과: 
# '4 + 3 - 2' = > '4 3 + 2 -' = 5.000000
# '4 + 3 - 4 / 2' = > '4 3 + 4 2 / -' = 5.000000
# '1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 3 * + 4 2 4 5 2 + - / * -' = 9.666667
# '( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 + 3 * 4 2 4 5 2 + - / * -' = 11.666667
