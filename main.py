#Аврамекно Екатерина Алексеевна ИСУ: 408103
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[30m'
END = '\u001b[0m'


def flag():
    for i in range(12):
        if i < 4:
            print(f'{RED}{"  " * 20}{END}')
        elif i > 3 and i < 8:
            print(f'{WHITE}{"  " * 20}{END}')
        else:
            print(f'{BLUE}{"  " * 20}{END}')
    print()
flag()

def graphic():
    plot_list = [[0 for i in range(11)] for i in range(11)]
    result = [0 for i in range(11)]

    for i in range(11):
        result[i] = 2 * i

    step = round(abs(result[0] - result[10]) / 10, 2)
    print(step)

    for i in range(11):
        for j in range(11):
            if j == 0:
                plot_list[i][j] = step * (9-i) + step

    for i in range(10):
        for j in range(11):
            if abs(plot_list[i][0] - result[10 - j]) < step:
                for k in range(10):
                    if 9 - k == j:
                        plot_list[i][k+1] = 1

    for i in range(10):
        line = ''
        for j in range(11):
            if j == 0:
                line += '\t' + str(int(plot_list[i][j])) + '\t'
            if plot_list[i][j] == 0:
                line += '..'
            if plot_list[i][j] == 1:
                line += '//'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9 10')
graphic()


def pattern(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print(f"{BLACK}  {END}", end='')
            else:
                print(f"{WHITE}  {END}", end='')
        for j in range(1, size):
            if i == j or i + j == size - 1:
                print(f"{BLACK}  {END}", end='')
            else:
                print(f"{WHITE}  {END}", end='')
        print()
pattern(10)


def sum():
    file = open('sequence.txt', 'r')
    list = []
    for number in file:
        list.append(float(number))
    file.close()
    sum_nechet = 0
    sum_chet = 0
    for i in range(len(list)):
        if i % 2 == 0:
            sum_nechet += list[i]
        else:
            sum_chet += list[i]
    print(round(sum_chet, 2), round(sum_nechet, 2))


nechet = []
chet = []
list = []
file = open('sequence.txt', 'r')
for number in file:
    list.append(float(number))
file.close()
sum_nechet = 0
sum_chet = 0
for i in range(len(list)):
    if i % 2 == 0:
        sum_nechet += list[i]
    else:
        sum_chet += list[i]
print('\n', round(sum_chet, 2), round(sum_nechet, 2))
c = int(abs(sum_chet))
n = int(abs(sum_nechet))
print(f'\n{WHITE}{"  " * ((c + n)*n//100)}{END}\n')
print(f'{WHITE}{"  " * ((c + n)*c//100)}{END}')
