num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
if num1 > num2:
    print('Наибольшее число', num1)
else:
    print('Наибольшее число', num2)

large = (num1 > num2) * num1 + (num2 >= num1) * num2
print('Наибольшее число', large)
