# simple calculator in python

def cal(x, y, opt):
    x = int(x)
    y = int(y)
    if opt == '+':
        return x + y
    elif opt == '-':
        return x - y
    elif opt == '*':
        return x * y
    elif opt == '/':
        return x / y
    else:
        print(" Enter a correct operator")


x = input('Enter the value of x: ')
y = input('Enter the value of y: ')
opt = input('Type operator:  (+ - * / )')

result = cal(x, y, opt)
print('The result is ' + str(result))
