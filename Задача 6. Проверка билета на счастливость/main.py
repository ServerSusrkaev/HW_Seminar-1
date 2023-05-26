resultOne = 0
resultTwo = 0

number = int(input('Введите 6-ти значное число: '))

resultOne += number // 100000
number = number % 100000

resultOne += number // 10000
number = number % 10000

resultOne += number // 1000
number = number % 1000


resultTwo += number // 100
number = number % 100

resultTwo += number // 10
number = number % 10
resultTwo += number

if resultOne == resultTwo:
    print('Happy ticket! :)')
else:
    print('Not a happy ticket :(')