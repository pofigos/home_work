road_long = 109
speed = int(input('Введите скорость: '))
time = int(input('Введите время в пути: '))
position = speed * time
if position < road_long:
    print('Байкер остановился на отметке', position)
else:
    print('Байкер остановился на отметке', position % road_long)
