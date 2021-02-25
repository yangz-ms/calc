def calc(expression):
    result = 0
    op = '+'
    current = 0
    for c in expression+'\uffff':
        if c >= '0' and c <= '9':
            # accumulate current number
            current = current * 10 + int(c)
        elif c == '+' or c == '-' or c == '\uffff':
            # start next operator, calculate current result
            if op == '+':
                result += current
            elif op == '-':
                result -= current
            current = 0
            op = c
    return str(result)

def test(expression, expected):
    result = calc(expression)
    if result == expected:
        print(f"Testing {expression}, got expected {expected}")
    else:
        print(f"Testing {expression}, expected {expected}, result {result}")

test("1+2+3", "6")
test("123+456 - 789", "-210")
test("123-456", "-333")
