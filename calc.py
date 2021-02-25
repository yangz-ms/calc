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

def calc2(expression):
    result = 0
    result2 = 0
    op = '+'
    current = 0
    for c in expression+'\uffff':
        if c >= '0' and c <= '9':
            # accumulate current number
            current = current * 10 + int(c)
        elif c == '+' or c == '-' or c == '*' or c == '/' or c == '\uffff':
            # start next operator, calculate current result
            if op == '+':
                result += result2
                result2 = current
            elif op == '-':
                result += result2
                result2 = -current
            elif op == '*':
                result2 *= current
            elif op == '/':
                result2 /= current
            current = 0
            op = c
    
    return str(result+result2)


def test(expression, expected, op=calc):
    result = op(expression)
    if result == expected:
        print(f"✅ Testing {expression}, got expected {expected}")
    else:
        print(f"❌ Testing {expression}, expected {expected}, result {result}")

test("1+2+3", "6", calc)
test("123+456 - 789", "-210", calc)
test("123-456", "-333", calc)

test("1+2+3", "6", calc2)
test("123+456 - 789", "-210", calc2)
test("123-456", "-333", calc2)
test("1*2*3", "6", calc2)
test("123+456*789", "359907", calc2)
test("1+2*3-4", "3", calc2)
test("1+2*3-5/4", "5.75", calc2)
test("1*2*3*4*5/6", "20.0", calc2)
