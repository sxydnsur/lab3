
import random

n = int(input("Введите число"))
i = 1
while i <= n-1:
    i += 1
    if i % 2 == 0:
        print(i)


# 2. Факториал (While). 

f = int(input("Введите число:"))
sum = 1
i = 1
while i<=f-1:
    i+=1
    sum*=i
    print(sum)

print("Факториал числа N = " , sum)

# 3. Поиск по номеру (break). 
while True:
    num_search = int(input("Введите число:"))
    if num_search == 42:
        break
print("Число 42 найдено , завершение работы программы!!!")

# /        4. Подсчет символов (строковые операции).
# //        Попросите пользователя ввести строку.
# //        Затем подсчитайте и выведите количество букв "а" в этой строке.

str1 = input("Введите слово")
count = 0

for char in str1:
    if char == 'а':
        count += 1

print(count)

# 5. Сумма цифр числа 


sum_of_digits = input("Введите число: ")
sum = 0

for i in range(len(sum_of_digits)):
    digit = sum_of_digits[i]
    if digit.isdigit():
        num_digit = int(digit)
        sum += num_digit

print(sum)

# //        6. Числа Фибоначчи while

fibonacci = int(input("Введите количество членов последовательности Фибоначчи: "))
sum = 0
i = 0
f1 = 0
f2 = 1
print(f1)
print(f2)

while i < fibonacci - 2:
    i += 1
    sum = f1 + f2
    f1 = f2
    f2 = sum
    print(sum)

# 7. Переверните строку 
str2 = input("Введите строку: ")
sum_str = ""

for i in range(len(str2) - 1, -1, -1):
    sum_str += str2[i]

print(sum_str)

# //        8. Пропустите четные 
sum = 0

while True:
    numberrr = int(input("write a numberrr"))

    if numberrr == 0:
        break
    if numberrr % 2 == 0:
        continue

    sum += numberrr

print(sum)


# 9. Угадайте число (break)

randnum = random.randint(1,100)
print(randnum)

while True:
    numwin = int(input("write a num \n"))
    if randnum > numwin:
        print("число больше чем это")
    if randnum < numwin:
        print("число меньше чем это")
    if randnum == numwin:
        print("winnn!!!")
        break


# //        10. Палиндром (строковые операции).
str222 = input("Введите строку: ")
pal = ""

for i in range(len(str222) - 1, -1, -1):
    pal += str222[i]

if pal == str222:
    print("Палиндром")
else:
    print("Не палиндром")


# //        11. Пронумеруйте до степени while

x = int(input("Введите число \n"))
y = int(input("Введите степень \n"))
i = 1
summm = 1
while i <= y:
    i+=1
    summm*=x

print(summm)


# 12. Подсчет простых чисел (While, Break).



n = int(input("Введите число n: "))
i = 2

while i <= n:
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
    i += 1


# 13. Обратное число (строковые операции). 
number = input("Введите число: ")
reversed_number = number[::-1]
print("Число в обратном порядке:", reversed_number)



#         14. Проверьте на первичность (продолжайте).
#               
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Введите число для проверки на простоту: "))

while True:
    if is_prime(number):
        print(f"{number} - простое число.")
        break
    else:
        print(f"{number} не является простым числом.")
        number += 1

#       15. Шифр Цезаря (строковые операции).

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

user_input = input("Введите строку: ")
shift = int(input("Введите сдвиг (целое число): "))

encrypted_text = caesar_cipher(user_input, shift)
print("Зашифрованная строка:", encrypted_text)

# 