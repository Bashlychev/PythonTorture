# # Строковый тип данных
# # Строковый тип данных, как и числовой, очень часто используется в программировании. В Python строковый тип данных имеет название str (сокращение от string — струна, ряд). 

# # Для создания строковой переменной (литерала), мы должны заключить необходимый текст в кавычки. В Python можно использовать как одинарные кавычки, так и двойные:

# # s1 = 'Python rocks!'
# # s2 = "Python rocks!"
# # Напомним, что по умолчанию, команда input() считывает именно строку текста:

# # s = input()  # переменная s имеет строковый тип str
# # Для задания пустой строки, мы используем две кавычки одинакового типа:

# # s1 = ''   # пустая строка
# # s2 = ' '  # строка состоящая из одного символа пробела
# # Не стоит путать пустую строку и строку состоящую из одного символа пробела. Это абсолютно разные строки.

# # Длина строки
# # Длиной строки называется количество символов из которых она состоит. Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина).

# # Следующий программный код:

# # s1 = 'abcdef'
# # length1 = len(s1)               # считаем длину строки из переменной s1
# # length2 = len('Python rocks!')  # считаем длину строкового литерала
# # print(length1)
# # print(length2)
# # выведет:

# # 6
# # 13
# #    При подсчете длины строки считаются все символы, включая пробелы.

# # Преобразование чисел в строку
# # Для преобразования строки к числу мы использовали функции int() и float(). Для обратного преобразования, то есть из числа в строку мы используем функцию str():

# # Рассмотрим следующий программный код:

# # num1 = 1777    # целое число
# # num2 = 17.77   # число с плавающей точкой
# # s1 = str(num1) # преобразовали целое число в строку '1777'
# # s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'
# # Иногда работать со строками намного проще, чем с числами. Даже если в условии задачи сказано, что дается число, нам ничто не мешает работать с ним как со строкой.

# # Конкатенация строк
# # Строки, как и числа, можно складывать. Операция сложения строк называется конкатенацией или сцеплением.

# # Рассмотрим следующий программный код:

# # s1 = 'ab' + 'bc'
# # s2 = 'bc' + 'ab'
# # s3 = s1 + s2 + '!!'
# # print(s1)
# # print(s2)
# # print(s3)
# # Результатом выполнения такого кода будет:

# # abbc
# # bcab
# # abbcbcab!!
# # Операция сложения строк в отличие от операции сложения чисел не является коммутативной, то есть, от перестановки мест слагаемых-строк результат меняется!

# # С помощью конкатенации строк можно эмулировать вывод данных, который раньше мы делали используя необязательные параметры sep и end. Следующие две строки кода делают одно и то же:

# # print('a', 'b', 'c', sep='*', end='!')
# # print()  # переход на новую строку
# # print('a' + '*' + 'b' + '*' + 'c' + '!')
# # Результатом выполнения такого кода будет:

# # a*b*c!
# # a*b*c!
# # Умножение строки на число
# # В Python также можно умножать строку на число. Такой оператор повторяет строку указанное количество раз.

# # Рассмотрим следующий программный код:

# # s = 'Hi' * 4
# # print(s)
# # Результатом выполнения такого кода будет:

# # HiHiHiHi
# # Оператор умножения строки на число (repetition) очень удобен на практике. Например, мы хотим распечатать строку состоящую из 75 символов -. Мы можем это сделать с помощью кода:

# # print('-' * 75)
# # Результатом выполнения такого кода будет:

# # ---------------------------------------------------------------------------
# #   Строку можно умножать на число, но нельзя умножать на строку.

# # Примечания
# # Примечание 1. Тройные кавычки в Python используются для многострочного (multiline) текста. Например,

# # text = '''Python is an interpreted, high-level, general-purpose programming language.
# # Created by Guido van Rossum and first released in 1991, Python design 
# # philosophy emphasizes code readability with its notable use of significant whitespace.'''
# # Примечание 2. На первый взгляд может показаться странным, что можно использовать как одинарные, так и двойные кавычки, однако такой подход позволяет очень легко добавлять в строку нужные кавычки:

# # s1 = 'Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"'
# # s2 = "Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'"
# # print(s1)
# # print(s2)
# # Результатом выполнения такого кода будет:

# # Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"
# # Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'

# # Что покажет приведенный ниже фрагмент кода?
# # str1 = '1'
# # str2 = str1 + '2' + str1
# # print(str2)
# # str3 = str2 + '3' + str2
# # print(str3)
# # str4 = str3 + '4' + str3
# # print(str4)

# # Что покажет приведенный ниже фрагмент кода?

# # mystr = '123' * 3 + '456' * 2 + '789' * 1
# # print(mystr)

# # Напишите программу, которая выводит текст:

# # "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

# # Примечание. Используйте конкатенацию строк.

# print( '"' + 'Python ' + 'is ' + 'a ' + 'great ' + 'language' + '!' + '"' + ', ' + 'said ' + 'Fred' + '. ' + '"' + 'I ' + "don't " + 'ever ' + 'remember ' + 'having ' + 'this ' + 'much ' + 'fun ' + 'before' + '.' + '"' )