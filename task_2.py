"""2. Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

def int_to_hex(n):
    return hex(n)

n = int(input("Введите целое число n: "))

print(int_to_hex(n))  