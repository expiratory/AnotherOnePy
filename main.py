# эта штука просто обнуляет 2 и 4 цифру пятизначного числа, ничего интересного
number = int(input("Введите пятизначное число: "))
def obnulenie(number):
    if number < 0:
        number = str(number)
        second_number = number[2]
        forth_number = number[4]
        second_number = str(0)
        forth_number = str(0)
        print(number[0] + number[1] + second_number + number[3] + forth_number + number[5])
    else:
        number = str(number)
        second_number = number[1]
        forth_number = number[3]
        second_number = str(0)
        forth_number = str(0)
        print(number[0] + second_number + number[2] + forth_number + number[4])

while True:
    if (number > 9999 and number < 100000) or (number < -9999 and number > -100000):
        obnulenie(number)
        break
    else:
        while True:
            number = int(input("Введите ПЯТИЗНАЧНОЕ ЧИСЛО: "))
            if (number > 9999 and number < 100000) or (number < -9999 and number > -100000):
                break
