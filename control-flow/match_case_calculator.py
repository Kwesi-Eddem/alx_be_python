first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))
operator = input('Choose the operation (+, -, *, /): ')

match operator:
    case '+':
        print(f'The result is {first + second}')
    case '-':
        print(f'The result is {first - second}')
    case '*':
        print(f'The result is {first * second}')
    case '/':
        if second == 0:
            print ('Cannot divide by zero')
        else:
            print(f'The result is {first / second}')
    case _:
        print(f'Invalid entry.')