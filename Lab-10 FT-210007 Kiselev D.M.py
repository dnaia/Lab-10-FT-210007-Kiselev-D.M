import logging

logging.basicConfig(level=logging.INFO, filename='logs_test20_Lab_10_FT_210007_Kiselev_D_M.txt', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")


# Красивый вывод
def answer(a, nominal):
    if a == 1 or a % 10 == 1:
        print(a, "купюра номиналом", nominal)
    elif a % 10 == 0 or (a % 10 >= 5 and a % 10 <= 9):
        print(a, "купюр номиналом", nominal)
    elif a % 10 != 0:
        print(a, "купюры номиналом", nominal)
    elif a % 10 != 0:
        print(a, "купюры номиналом", nominal)


one = 1
two = 2
four = 4
eight = 8
sixteen = 16
thirtytwo = 32
sixtyfour = 64

# Счетчики для каждой купюры
onecounter = 0
twocounter = 0
fourcounter = 0
eightcounter = 0
sixteencounter = 0
thirtytwocounter = 0
sixtyfourcounter = 0

counter1 = 0  # Вспомогательный счетчик
while counter1 != 1:  # Проверка, чтобы ввели натуральное число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        n = int(input('Введите натуральное число N '))
        logging.info('Вводят натуральное число N')
        while n <= 0:  # Проверка, чтобы ввели положительное число
            print("Введите положительное число!")
            # logging.warning('Ввели число, меньшее единицы')
            n = int(input('Введите натуральное число N '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
        logging.error('Ввели не число!')
    else:
        counter1 += 1
        logging.info('Ввели корректное число({})'.format(n))

helpn = n  # Вспомогательная n

while helpn > 0:  # Самый большой номинал
    first = helpn - sixtyfour
    helpn = helpn - sixtyfour  # Проверяем макс число купюр по 64
    sixtyfourcounter += 1
    logging.info('Считают примерное кол-во купюр по 64 - ({})'.format(sixtyfourcounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + sixtyfour
    sixtyfourcounter = sixtyfourcounter - 1
    logging.info('Узнают точное кол-во купюр по 64 - ({})'.format(sixtyfourcounter))

while helpn > 0:  # от остатка купюр по 64, проверяем макс число купюр 32
    helpn = helpn - thirtytwo
    thirtytwocounter += 1
    logging.info('Считают примерное кол-во купюр по 32 - ({})'.format(thirtytwocounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + thirtytwo
    thirtytwocounter = thirtytwocounter - 1
    logging.info('Узнают точное кол-во купюр по 32 - ({})'.format(thirtytwocounter))

while helpn > 0:  # от остатка купюр по 32, проверяем макс число купюр 16
    helpn = helpn - sixteen
    sixteencounter += 1
    logging.info('Считают примерное кол-во купюр по 16 - ({})'.format(sixteencounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + sixteen
    sixteencounter = sixteencounter - 1
    logging.info('Узнают точное кол-во купюр по 16 - ({})'.format(sixteencounter))

while helpn > 0:  # от остатка купюр по 16, проверяем макс число купюр 8
    helpn = helpn - eight
    eightcounter += 1
    logging.info('Считают примерное кол-во купюр по 8 - ({})'.format(eightcounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + eight
    eightcounter = eightcounter - 1
    logging.info('Узнают точное кол-во купюр по 8 - ({})'.format(eightcounter))

while helpn > 0:  # от остатка купюр по 8, проверяем макс число купюр 4
    helpn = helpn - four
    fourcounter += 1
    logging.info('Считают примерное кол-во купюр по 4 - ({})'.format(fourcounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + four
    fourcounter = fourcounter - 1
    logging.info('Узнают точное кол-во купюр по 4 - ({})'.format(fourcounter))

while helpn > 0:  # от остатка купюр по 4, проверяем макс число купюр 2
    helpn = helpn - two
    twocounter += 1
    logging.info('Считают примерное кол-во купюр по 2 - ({})'.format(twocounter))

if helpn < 0:  # n меньше нуля, такого быть не может
    helpn = helpn + two
    twocounter = twocounter - 1
    logging.info('Узнают точное кол-во купюр по 2 - ({})'.format(twocounter))

while helpn > 0:  # от остатка купюр по 2, проверяем макс число купюр 1
    helpn = helpn - one
    onecounter += 1
    logging.info('Узнают точное кол-во купюр по 1 - ({})'.format(onecounter))

if sixtyfourcounter != 0:  # Вывод кол-ва купюр
    a = sixtyfourcounter
    nominal = sixtyfour
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 64 - ({})'.format(sixtyfourcounter))

if thirtytwocounter != 0:  # Вывод кол-ва купюр
    a = thirtytwocounter
    nominal = thirtytwo
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 32 - ({})'.format(thirtytwocounter))

if sixteencounter != 0:  # Вывод кол-ва купюр
    a = sixteencounter
    nominal = sixteen
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 16 - ({})'.format(sixteencounter))

if eightcounter != 0:  # Вывод кол-ва купюр
    a = eightcounter
    nominal = eight
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 8 - ({})'.format(eightcounter))

if fourcounter != 0:  # Вывод кол-ва купюр
    a = fourcounter
    nominal = four
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 4 - ({})'.format(fourcounter))

if twocounter != 0:  # Вывод кол-ва купюр
    a = twocounter
    nominal = two
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 2 - ({})'.format(twocounter))

if onecounter != 0:  # Вывод кол-ва купюр
    a = onecounter
    nominal = one
    answer(a, nominal)
    logging.info('Выводит кол-во купюр по 1 - ({})'.format(onecounter))
