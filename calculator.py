def calculator():
    while True:  
        a = float(input('Number: '))
        op = input('Operator (+*-/): ')
        b = float(input('Number: '))
        
        if op == '+':
            res = a + b
            print(a, '+',  b, '=', res)
        elif op == '*':
            res = a * b
            print(a, 'x',  b, '=', res)
        elif op == '-':
            res = a - b
            print(a, '-',  b, '=', res)
        elif op == '/':
            if b == 0:
                print('You cannot divided by zero')
            else:
                res = a / b
                print(a, '/',  b, '=', res)
        else:
            print("Invalid Operator:'{}'".format(op))
            return
    

calculator()
