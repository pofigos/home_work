num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 == num2 == num3:
    print(3)
elif num1 != num2 & num1 != num3 & num2 != num3:
    print(0)
else:
    print(2)
