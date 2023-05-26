# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите 3-х значное число: "))
result = 0

digit = number // 100
result += digit

number = number % 100
digit = number // 10
result += digit

digit = number % 10
result += digit

print(result)