coupe = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
place = int(input('Введите номер места: '))
if place > 0 and place <= 4:
    print ('Купе №:',coupe[0])
elif place > 4 and place <= 8:
    print('Купе №:',coupe[1])
elif place > 8 and place <= 12:
    print('Купе №:',coupe[2])
elif place > 12 and place <= 16:
    print('Купе №:',coupe[3])
elif place > 16 and place <= 20:
    print('Купе №:',coupe[4])
elif place > 20 and place <= 24:
    print('Купе №:',coupe[5])
elif place > 24 and place <= 28:
    print('Купе №:',coupe[6])
elif place > 28 and place <= 32:
    print('Купе №:',coupe[7])
elif place > 32 and place <= 36:
    print('Купе №:',coupe[8])
elif type(place) != int and len(place) == 0:
    print('Введите число!')
