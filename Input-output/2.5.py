# Возведение в степень
# Оператор возведения в степень a ** n возводит число 
# �
# a в степень 
# �
# n. 

# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** (-1))

# Обратите внимание: оператор возведения в степень (**) является правоассоциативным (значение выражения вычисляется справа налево) в соответствии с правилами математики. Таким образом, выражение x ** y ** z вычисляется как x ** (y ** z).

# Результатом работы следующей программы:

# print(2 ** 2 ** 3)     # 2 ** (2 ** 3) = 2 ** 8

# Целочисленное деление
# Для положительных чисел оператор целочисленного деления ведёт себя как обычное деление, за исключением того, что он отбрасывает десятичную часть результата. Рассмотрим работу данного оператора на примерах:

# print(10 // 3)
# print(10 // 4)
# print(10 // 5)
# print(10 // 6)
# print(10 // 12)

# При делении отрицательных чисел необходимо помнить, что результат целочисленного деления не превосходит частное. Другими словами, округление берётся в меньшую сторону (число 
# −
# 4
# −4 меньше, чем число 
# −
# 3
# −3).

# Результатом работы следующей программы:

# print(10 // 3)
# print(-10 // 3)

# будут числа:

# # 3   # округление в меньшую сторону
# -4  # округление в меньшую сторону

# Деление с остатком
# Оператор деления с остатком возвращает остаток от деления двух целых чисел. Рассмотрим работу данного оператора на примерах:

# print(10 % 3)
# print(10 % 4)
# print(10 % 5)
# print(10 % 6)
# print(10 % 12)
# print(10 % 20)

# Геометрическая прогрессия
# Геометрической прогрессией называется последовательность чисел 
# �
# 1
# ,
# �
# 2
# ,
# …
# ,
# �
# �
# b 
# 1
# ​
#  ,b 
# 2
# ​
#  ,…,b 
# n
# ​
#  , каждое из которых, начиная с 
# �
# 2
# b 
# 2
# ​
#  , получается из предыдущего умножением на одно и то же постоянное число 
# �
# q (знаменатель прогрессии), то есть

# �
# �
# =
# �
# �
# −
# 1
# ⋅
# �
# b 
# n
# ​
#  =b 
# n−1
# ​
#  ⋅q

# Если известен первый член прогрессии и её знаменатель, то 
# �
# n-ый член геометрической прогрессии находится по формуле

# �
# �
# =
# �
# 1
# ⋅
# �
# �
# −
# 1
# b 
# n
# ​
#  =b 
# 1
# ​
#  ⋅q 
# n−1
 
# Входные данные
# На вход программе подаётся три целых числа: 
# �
# 1
# b 
# 1
# ​
#  , 
# �
# q и 
# �
# n, каждое на отдельной строке.

# Выходные данные
# Программа должна вывести 
# �
# n-ый член геометрической прогрессии.

# a,b,c =int(input()), int(input()), int(input())
# print(a*b**(c-1))

# Расстояние в метрах
# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

# Формат входных данных
# На вход программе подаётся натуральное число – количество сантиметров.

# Формат выходных данных
# Программа должна вывести одно число – полное число метров.

# a = int(input())
# print(a // 100)

#  Мандарины
# �
# n школьников делят 
# �
# k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

# Формат входных данных
# На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику, и количество мандаринов, которое останется в корзине, каждое на отдельной строке.

# n,k =int(input()), int(input())
# print(k//n)
# print(k%n)

# Сама неотвратимость 🌶️
# Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.

# Формат входных данных
# На вход дается число целое 
# �
# n – население Вселенной.

# Формат выходных данных
# Программа должна вывести одно число – количество выживших.

# n = int(input())
# print(n//2+n%2)

# В купейном вагоне имеется 
# 9
# 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 
# 1
# 1).
# Формат входных данных
# На вход программе подаётся целое число – место с заданным номером в вагоне.

# Формат выходных данных
# Программа должна вывести одно число – номер купе, в котором находится указаное место.
# a = int(input())
# print((a+3)//4)

# Пересчет временного интервала
# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.

# Формат входных данных
# На вход программе подаётся целое число – количество минут.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# a = int(input())
# print(a,'мин - это', a//60 ,'час',a%60 ,'минут.')

# Обработка цифр числа
# При помощи операции нахождения остатка и целочисленного деления можно достаточно несложно вычислить любую цифру числа.

# Рассмотрим программу получения цифр двузначного числа:

# num = 17
# a = num % 10
# b = num // 10

# print(a)
# print(b)

# Запомни: последняя цифра числа определяется всегда как остаток от деления числа на 10 (% 10). Чтобы отщепить последнюю цифру от числа, необходимо разделить его нацело на 10 (// 10).

# Рассмотрим программу получения цифр трёхзначного числа:

# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100

# print(a)
# print(b)
# print(c)

# Алгоритм получения цифр 
# �
# n-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру 
# �
# n-значного числа num:

# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.

# Решение задач
# Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.

# Решение. Число единиц – это последняя цифра числа, число десятков – первая цифра. Чтобы получить последнюю цифру любого числа, нужно найти остаток от деления числа на 
# 10
# 10. Чтобы найти первую цифру двузначного числа, нужно поделить число нацело на 
# 10
# 10. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)

# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Сумма цифр =', last_digit + first_digit)

# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10

# print('Искомое число =', last_digit * 10 + first_digit)

# Задача 4. Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую).

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100

# print(digit1, digit2, digit3, sep=',')

# для чайников:

# 123456789  // 1 % 10 ---> 9                (единицы)

# 123456789   // 10 % 10 ---> 8               (десятки)

# 123456789  // 100 % 10 ---> 7               (сотни)

# 123456789  // 1000 % 10 ---> 6             (тысячи)

# 123456789  // 10000 % 10 ---> 5           (десятки тысяч)

# 123456789  // 100000 % 10 ---> 4         (сотни тысяч)

# 123456789  // 1000000 % 10 ---> 3       (миллионы)

# 123456789  // 10000000 % 10 ---> 2     (десятки миллионов)

# 123456789  // 100000000 % 10 ---> 1   (сотни миллионов)

# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.

# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

# a = int(input())
# num3 = a // 1 % 10
# num2 = a // 10 % 10
# num1 = a // 100 % 10

# print('Сумма цифр =', num1+num2+num3)
# print('Произведение цифр =', num1*num2*num3)

# Перестановка цифр
# Дано трехзначное число 

# abc
#  , в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

# Формат входных данных
# На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

# Формат выходных данных
# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: 
# abc,acb,bac,bca,cab,cba.

# num = int(input())
# c = num // 1 % 10
# b = num // 10 % 10
# a = num // 100 % 10
# print(a,b,c,sep='')
# print(a,c,b,sep='')
# print(b,a,c,sep='')
# print(b,c,a,sep='')
# print(c,a,b,sep='')
# print(c,b,a,sep='')

# Четырёхзначное число
# Напишите программу для нахождения цифр четырёхзначного числа.

# Формат входных данных
# На вход программе подаётся положительное четырёхзначное целое число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# num = int(input())
# d = num // 1 % 10
# c = num // 10 % 10
# b = num // 100 % 10
# a = num // 1000 % 10

# print('Цифра в позиции тысяч равна', a)
# print('Цифра в позиции сотен равна', b)
# print('Цифра в позиции десятков равна', c)
# print('Цифра в позиции единиц равна', d)



