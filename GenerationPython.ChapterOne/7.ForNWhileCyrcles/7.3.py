# Тема урока: частые сценарии
# Подсчет количества
# Вычисление суммы и произведения
# Обмен значений переменных
# Сигнальные метки
# Определение максимума и минимума
# Расширенные операторы присваивания (+=, -=, //= и т.д.)
# Аннотация. Рассмотрим частые сценарии при написании циклов.

# Подсчет количества
# Нередко нужно, чтобы наши программы подсчитывали, сколько раз что-либо произошло. К примеру, видеоигра может подсчитывать количество поворотов персонажа, или математическая программа может считать, как много чисел обладают некоторым свойством. Ключ к подсчету – использование переменной счетчика.

# Напишем программу, которая считывает 
# 10
# 10 чисел и определяет, сколько из них больше 
# 10
# 10.

# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1

# print('Было введено', counter, 'чисел, больших 10.')
# Каждый раз, когда мы считываем число, большее 
# 10
# 10, мы добавляем 
# 1
# 1 к нашему текущему значению переменной counter. В программе это реализовано в строке counter = counter + 1. Обратите внимание на начальное значение переменной счетчика counter = 0. Без начального значения мы получили бы ошибку, поскольку, дойдя до строки counter = counter + 1, Python ничего не знал бы о переменной counter. Строка кода counter = counter + 1 означает: возьми старое значение переменной counter, прибавь к нему 
# 1
# 1 и переприсвой переменной это значение. Если не придать переменной начальное значение, то непонятно, к чему прибавлять 
# 1
# 1 в самый первый раз.

# Подсчет количества – это очень частый сценарий. Он состоит из двух шагов:

# Создание переменной счетчика, и придание ей первоначального значения: counter = 0;
# Увеличение переменной счетчика на 
# 1
# 1: counter = counter + 1.
# Часто при написании программ требуется использовать несколько счетчиков. Модифицируем предыдущую программу: посчитаем еще и количество нулей среди введенных чисел.

# counter1 = 0
# counter2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1

# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )
# Рассмотрим еще один пример: подсчитать количество чисел из диапазона 
# [
# 1
# ;
# 100
# ]
# [1;100], квадрат которых оканчивается на 
# 4
# 4.

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1

# print(counter)
# Мы используем функцию range() с двумя параметрами для генерации последовательности чисел от 
# 1
# 1 до 
# 100
# 100. Каждый раз, когда переменная i последовательно принимает значения от 
# 1
# 1 до 
# 100
# 100, мы проверяем условие: i**2 % 10 == 4 (оканчивается ли квадрат числа i на 
# 4
# 4).

#    Для переменной счетчика удобно использовать имя counter (или более сокращенно cnt). 

# Вычисление суммы и произведения
# Наравне с подсчетом количества по частоте стоит задача вычисления суммы. К примеру, видеоигра должна считать сумму очков. В таком случае начальное значение переменной будет равно 
# 0
# 0, а далее оно будет увеличиваться на некоторое количество заработанных очков, скажем на 
# 10
# 10. Мы пишем следующий код:

# score = 0
# ...
# score = score + 10
# Напишем программу, которая считывает 
# 10
# 10 чисел и определяет сумму тех из них, которые больше 
# 10
# 10.

# total = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num

# print('Сумма чисел больших 10 равна',  total)
# Каждый раз, когда программа считывает число, большее 
# 10
# 10, она добавляет его к текущему значению переменной total. Это реализовано в строке total = total + num. Обратите внимание на начальное значение переменной-сумматора total = 0. Без начального значения мы получили бы ошибку, поскольку, дойдя до строки total = total + num, Python ничего не знал бы о переменной total . Строка кода total = total + num означает: возьми старое значение переменной total, прибавь к нему num и переприсвой переменной это значение. Если не придать переменной начальное значение, то не к чему прибавлять num в самый первый раз.

# Подсчет суммы состоит из двух шагов:

# Создание переменной сумматора и придание ей первоначального значения: total = 0;
# Увеличение переменной сумматора на нужное число: total = total + num.
# Напишем программу, которая считает сумму натуральных чисел от 
# 1
# 1 до 
# 100
# 100:

# total = 0
# for i in range(1, 101):
#     total = total + i

# print('Сумма равна', total)
# Рассмотрим еще один пример: напишем программу, которая запрашивает 
# 10
# 10 целых чисел и находит их среднее значение:

# total = 0
# for _ in range(10):
#     num = int(input())
#     total = total + num

# average = total / 10
# print('Среднее значение равно', average)
# Аналогичным образом вычисляется произведение. При вычислении произведения начальное значение переменной мультипликатора мы устанавливаем равным 
# 1
# 1, в отличие от сумматора, где оно равно 
# 0
# 0.

#     Для переменной сумматора и мультипликатора удобно использовать имя total. 

# Обмен значений переменных
# Очень часто нам требуется обменять значения двух переменных x и y. Начинающие программисты иногда пишут такой код:

# x = y
# y = x
# Однако он не работает. Предположим, что x = 3 и y = 5. Первая строка присвоит переменной x значение 
# 5
# 5, что правильно, однако вторая строка установит значение переменной y в 
# 5
# 5, поскольку значение x уже равно 
# 5
# 5. Для решения задачи мы можем использовать временную переменную:

# temp = x
# x = y
# y = temp
# Такой код пишут почти во всех языках программирования. Однако в Python есть и более простой способ. Мы можем написать так:

# x, y = y, x
# В результате выполнения такого кода Python поменяет значения переменных x и y местами.

# Сигнальные метки
# Сигнальная метка (флажок) может использоваться, когда надо, чтобы одна часть программы узнала о происходящем в другой части программы.
# Напишем программу, определяющую, что натуральное число является простым:

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False

# if num == 1:
#     print('Это единица, она не простая и не составная') 
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# Напомним, что число является простым, если оно не имеет делителей, кроме 
# 1
# 1 и самого себя. Вышеприведенная программа работает следующим образом: начальное значение переменной флага равно True, что говорит о том, что число является простым. Затем мы перебираем все числа от 
# 2
# 2 до num - 1 (включительно). Если одно из этих значений оказывается делителем числа num, тогда число num является составным и мы устанавливаем значение флага False. Как только цикл завершен, мы проверяем, установлен флаг в True или нет. Если это так, мы знаем, что делитель найден не был и число является простым. В противном случае число является составным.

# Флаговые переменные могут иметь более осмысленное название. Например, в случае с проверкой числа на простоту, название флаговой переменной могло бы быть is_prime.

# Максимум и минимум
# Поиск наибольшего или наименьшего значения в некоторой последовательности чисел – также частая задача в программировании. Напишем программу, которая считывает 
# 10
# 10 положительных чисел и находит среди них наибольшее число.

# largest = 0
# for _ in range(10):
#     num = int(input())    
#     if num > largest:
#         largest = num

# print('Наибольшее число равно', largest) 
# Мы устанавливаем начальное значение переменной largest  в 
# 0
# 0. Далее программа считывает 
# 10
# 10 чисел, и если какое-то из них оказывается больше текущего значения largest, переприсваивает его. В качестве начального значения взято число 
# 0
# 0, поскольку мы знаем, что все числа положительны (а 
# 0
# 0 является максимальным неположительным числом). Таким образом, уже первое сравнение приведет к переприсваиванию.

# Распространен подход, когда в качестве начального значения переменной сразу принимается первый элемент последовательности. Напишем программу, которая считывает 
# 10
# 10 чисел (необязательно положительных) и находит среди них наибольшее:

# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num

# print('Наибольшее число равно', largest) 
# Для нахождения наименьшего значения последовательности следует поменять знак неравенства (>) на противоположный (<). В таком случае название переменной largest стоит заменить на smallest.

#     Для переменных, хранящих наибольшее и наименьшее значения, подходят имена largest и smallest соответственно.

# Расширенные операторы присваивания
# Довольно часто программы имеют инструкции присваивания, в которых переменная на левой стороне от оператора = также появляется на правой от него стороне. Например, 

# counter = counter + 1
# На правой стороне оператора присваивания 1 прибавляется к переменной counter. Полученный результат затем присваивается переменной counter, заменяя первоначальное значение. По сути, это строка кода добавляет 1 к counter. Еще один пример такой инструкции мы видели при подсчете суммы:

# total = total + num
# Эта инструкция присваивает значение выражения total + num переменной total. В результате исполнения этой инструкции число num прибавляется к значению total.

# Различные инструкции присваивания (в каждой инструкции x = 6)
# Инструкция	Что она делает	Значение x после инструкции
# x = x + 4	Прибавляет 4 к x	10
# x = x - 3	Вычитает 3 из x	3
# x = x * 10	Умножает x на 10	60
# x = x / 4	Делит x на 4	1.5
# x = x // 4	Делит нацело x на 4	1
# x = x % 4	Находит остаток от деления x на 4	2
# Эти типы операций находят широкое применение в программировании. Для удобства Python предлагает расширенные операторы присваивания. Расширенные операторы не требуют, чтобы программист дважды набирал имя переменной. Приведенную ниже инструкцию:

# total = total + num
#  можно переписать как

# total += num
# Точно так же инструкцию

# counter = counter + 1
# можно переписать как

# counter += 1
# Оператор	Пример использования	Эквивалент
# +=	x += 5	x = x + 5
# -=	x -= 2	x = x - 2
# *=	x *= 10	x = x * 10
# /=	x /= 4	x = x / 4
# //=	x //= 4	x = x // 4
# %=	x %= 4	x = x % 4
# Примечания
# Примечание 1. Аналогичным образом можно менять местами значения трех и более переменных.

# a, b, c, d = b, c, d, a
# Примечание 2. Очень часто сигнальные метки называют flag.

# Примечание 3. Поскольку в Python есть встроенные функции max() и min(), то давать такие названия для максимального и минимального значения не очень хорошо. Куда лучше использовать названия largest и smallest или mx и mn.

# Примечание 4. Сумму чисел от 1 до 100, можно вычислить и без цикла: 
# Сумма
# =
# 1
# +
# 100
# 2
# ⋅
# 100
# =
# 5050.
# Сумма= 
# 2
# 1+100
# ​
#  ⋅100=5050.
# Действительно, числа от 
# 1
# 1 до 
# 100
# 100, можно разбить на 
# 50
# 50 пар, сумма в которых равна 
# 101
# 101: 
# 1
# +
# 100
# =
# 101
# ,
# 2
# +
# 99
# =
# 101
# ,
# 3
# +
# 98
# =
# 101
# ,
# …
# 50
# +
# 51
# =
# 101.
# 1+100=101,2+99=101,3+98=101,…50+51=101.
# В начальной школе, где учился математик Карл Фридрих Гаусс (6 лет), учитель, чтобы занять класс на продолжительное время самостоятельной работой, дал задание ученикам – вычислить сумму всех натуральных чисел от 
# 1
# 1 до 
# 100
# 100. Маленький Гаусс ответил на вопрос почти мгновенно, применив указанный способ подсчета, чем невероятно удивил всех и, прежде всего, учителя.


# num1 = 4
# num2 = 6
# num1 = num1 + num2
# num1 = num1*num1
# print(num1)

# Количество чисел
# На вход программе подаются два целых числа 
# �
# a и 
# �
# b 
# (
# �
# ≤
# �
# )
# (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от 
# �
# a до 
# �
# b включительно, куб которых оканчивается на 
# 4
# 4 или 
# 9
# 9.

# Формат входных данных
# На вход программе подаются два целых числа 
# �
# a и 
# �
# b 
# (
# �
# ≤
# �
# )
# (a≤b).

# Формат выходных данных
# Программа должна вывести одно целое число в соответствии с условием программы.

# Примечание. Куб числа 
# �
# a – это его третья степень 
# �
# 3
# a 
# 3
#  .

# a,b = int(input()),int(input())
# counter = 0
# for i  in range (a,b+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#         counter = counter+1
# print(counter)

# Сумма чисел
# На вход программе подается натуральное число 
# �
# n, а затем 
# �
# n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел (не включая само число 
# �
# n). 

# Формат входных данных
# На вход программе подаются натуральное число 
# �
# n, а затем 
# �
# n целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести сумму данных чисел.

# n = int (input())
# total = 0
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)

# симптотическое приближение
# На вход программе подается натуральное число 
# �
# n. Напишите программу, которая вычисляет значение выражения
# (
# 1
# +
# 1
# 2
 
# +
# 1
# 3
# +
# …
# +
# 1
# �
# )
# −
# ln
# ⁡
# (
# �
# )
# .
# (1+ 
# 2
# 1
# ​
#   + 
# 3
# 1
# ​
#  +…+ 
# n
# 1
# ​
#  )−ln(n).

# Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

# from math import *

# n = int(input())
# total = 0
# for i in range(1,n+1):
#     total = total + 1/i
# print(total - log(n))

# Сумма чисел 2
# На вход программе подается натуральное число 
# �
# n. Напишите программу, которая подсчитывает сумму тех чисел от 
# 1
# 1 до 
# �
# n (включительно), квадрат которых оканчивается на 
# 2
# ,
# 5
# 2,5 или 
# 8
# 8.

# Формат входных данных
# На вход программе подается натуральное число 
# �
# n.

# Формат выходных данных
# Программа должна вывести единственное число в соответствии с условием задачи.

# Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 
# 0
# 0.


# n = int(input())
# total = 0
# for i in range(1,n):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         total = total + i
# print(total)

# Факториал
# На вход программе подается натуральное число 
# �
# n. Напишите программу, которая вычисляет 
# �
# !
# n!.

# Входные данные
# На вход программе подается натуральное число 
# �
# ,
# (
# �
# ≤
# 12
# )
# n,(n≤12).

# Выходные данные
# Программа должна вывести единственное число в соответствии с условием задачи.

# Примечание. Факториалом натурального числа 
# �
# n, называется произведение всех натуральных чисел от 
# 1
# 1 до 
# �
# n, то есть
# �
# !
# =
# 1
# ⋅
# 2
# ⋅
# 3
# ⋅
# …
# ⋅
# �
# n!=1⋅2⋅3⋅…⋅n

# from math import *
# n = int(input())
# print(factorial(n))

# Без нулей
# Напишите программу, которая считывает 
# 10
# 10 чисел и выводит произведение отличных от нуля чисел.

# Формат входных данных
# На вход программе подаются 
# 10
# 10 целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести произведение отличных от нуля чисел.

# Примечание. Гарантируется, что хотя бы одно из 
# 10
# 10 чисел является ненулевым.