# эта штука просто обнуляет 2 и 4 цифру пятизначного числа, ничего интересного
number = int(input("Введите пятизначное число: "))
def obnuleniePolozhitelnogo(number):
    number = str(number)
    second_number = number[1]
    forth_number = number[3]
    second_number = str(0)
    forth_number = str(0)
    print(number[0] + second_number + number[2] + forth_number + number[4])

def obnulenieOtritsatelnogo(number):
    number = str(number)
    second_number = number[2]
    forth_number = number[4]
    second_number = str(0)
    forth_number = str(0)
    print(number[0] + number[1] + second_number + number[3] + forth_number + number[5])

while True:
    if number > 9999 and number < 100000:
        obnuleniePolozhitelnogo(number)
        break
    elif number < -9999 and number > -100000:
        obnulenieOtritsatelnogo(number)
        break
    else:
        while True:
            number = int(input("Введите ПЯТИЗНАЧНОЕ ЧИСЛО: "))
            if (number > 9999 and number < 100000) or (number < -9999 and number > -100000):
                break
