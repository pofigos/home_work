num1x = int(input('Введите первое число позиции ладьи: '))
num1y = int(input('Введите второе число позиции ладьи: '))
num2x = int(input('Введите первое число цели ладьи: '))
num2y = int(input('Введите второе число цели ладьи: '))

if (abs(num1x - num2x) <= 8) & (abs(num1y - num2y) == 0):
    print('TES')
elif (abs(num1x - num2x) == 0) & (abs(num1y - num2y) <= 8):
    print('TES')
else:
    print('NO')
