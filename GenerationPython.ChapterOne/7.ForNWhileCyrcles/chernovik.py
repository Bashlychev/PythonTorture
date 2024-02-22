# 7.1
# Python is awesome
# a = 'Python is awesome!'
# for i in range(1,11):
#     print(a)

# Повторяй за мной 1
# a = input()
# b = int(input())
# for i in range(1,b+1):
#     print(a)

# Последовательность символов
# a = 'AAA'
# b = 'BBBB'
# t = 'TTTTT'
# for i in range (1,7):
#     print(a)
# for i in range (1,6):
#     print(b)
# print('E')
# for i in range (1,10):
#     print(t)
# print('G')

# # Звездный прямоугольник
# n = int(input())
# for i in range (1,n+1):
#     print('*'*19)

# Повторяй за мной 2
# n = (input())
# for i in range(10):
#     print(i,n)

# Квадрат числа
# n = int(input())
# for i in range(0,n+1):
#     print('Квадрат числа', i, 'равен',i**2)

# Звездный треугольник
# n = int(input())
# for i in range (n+1):
#     print('*'*(n-i))

# Популяция
# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#      g = (m * (p / 100 + 1) ** i)
#      print(i+1,g)
    
# 7.2
# Последовательность чисел 1
# m,n = int(input()),int(input())
# for i in range(m,n+1):
#     print(i)

# Последовательность чисел 2 🌶️
# m, n = int(input()),int(input())
# if m < n:
#      for i in range(m,n+1):
#           print(i)
# elif m > n:
#      for j in range(m,n-1,-1):
#           print(j)
# else: print(m)

# Последовательность чисел 3 🌶️
# m,n = int(input()),int(input())
# for i in range(m,n-1,-1):
#      if i % 2 != 0:
#           print(i)

# Последовательность чисел 4
# m,n = int(input()),int(input())
# for i in range(m,n+1):
#     if i % 17 == 0 or i // 1 % 10 == 9 or i % 3 == 0 and i % 5 == 0:
#         print(i)

# Таблица умножения
# n = int(input())
# for i in range(1,11):
#     print(n,'x',i,'=',n*i)

# 7.3
# Количество чисел
# a,b = int(input()),int(input())
# counter = 0
# for i in range(a,b+1):
#     if i**3 % 10 == 4 or i**3 % 10 == 9:
#           counter += 1
# print(counter)

# Сумма чисел
# n = int(input())
# counter = 0
# for i in range(1,n+1):
#     n1 = int(input())
#     counter += n1
# print(counter)

# Асимптотическое приближение
# from math import *
# n = int(input())
# counter = 0
# for i in range(1,n+1):
#      counter += 1/i
# print(counter-log(n))

# Сумма чисел 2
# n = int(input())
# counter = 0
# for i in range(1,n+1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         counter += i
# print(counter)

# Факториал
# n = int(input())
# counter = 1
# for i in range(1,n+1):
#     counter *= i
# print(counter)

# Без нулей
# total = 1
# for i in range (10):
#     n = int(input())
#     if n != 0:
#      total *=n
# print(total)

# Сумма делителей
# n = int(input())
# counter = 0
# for i in range(1,n+1):
#     if n % i == 0:
#      counter += i
# print(counter)

# Знакочередующаяся сумма
# n = 5
# counter = 0
# for i in range(1,n+1):
#     counter += ((-1)**(i+1))*i
# print(counter)

# Наибольшие числа 🌶️🌶️
# n = int(input())
# maxx1 = 0
# maxx2 = 1
# for i in range (1,n+1):
#     num = int(input())
#     if num > maxx1:
#         maxx2 = maxx1
#         maxx1 = num
#     elif num > maxx2:
#         maxx2 = num
# print(maxx1)
# print(maxx2)

# Only even numbers 🌶️
# flag = True
# for i in range(1,11):
#     num = int(input())
#     if num % 2 != 0:
#         flag = False
#         break
# if flag == False:
#     print('NO')
# else: print('YES')

# Последовательность Фибоначчи 🌶️
# n = int(input())
# f1 = 1
# f2 = 1
# for i in range(n):
#     print(f1,end=' ')
#     f1,f2 = f2,f1+f2

# 7.4

# До КОНЦА 1
# a = input()
# while a != 'КОНЕЦ':
#     print(a)
#     a = input()

# До КОНЦА 2
# a = input()
# while a != 'КОНЕЦ' and a != 'конец':
#     print(a)
#     a = input()

# Количество членов
# a = input()
# count = 0
# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#     count += 1
#     a = input()
# print(count)

# Пока делимся
# a = int(input())
# while a % 7 == 0:
#     print(a)
#     a = int(input())

# Сумма чисел
# n = int(input())
# count = 0
# while n >-1:
#     count +=n
#     n = int(input())
# print(count)

# Количество пятерок
# n = int(input())
# five = 0
# while  0 < n < 6:
#     if n == 5:
#         five +=1
#     n = int(input())
# print(five)

# Ведьмаку заплатите чеканной монетой
# n = int(input())
# count = 0
# while n >= 25:
#     count += 1
#     n = n - 25
# while n >= 10:
#     count += 1
#     n = n - 10
# while n >= 5:
#     count += 1
#     n = n - 5
# while n >= 1:
#     count +=1
#     n = n - 1
# print(count)

# 7.5
# Обратный порядок 1
# n = int(input())
# total = 0
# while n != 0:
#     last_digit = n % 10
#     total +=1
#     print(last_digit)
#     n = n //10
    
# Обратный порядок 2
# n = int(input())
# total = 0
# while n !=0:
#  last_digit = n % 10
#  total +=1
#  print(last_digit,end='')
#  n = n //10

# max и min
# n = 26670
# maxx = 0
# minn = 9
# while n >0:
#     last_digit = n % 10
#     if last_digit > maxx:
#         maxx = last_digit
#     if last_digit < minn:
#         minn = last_digit
#     n = n // 10
# print('Максимальная цифра равна',maxx)
# print('Минимальная цифра равнаэ',minn)

# Все вместе
# n = int(input())
# sum = 0
# count = 0
# quantity = 0
# total = 1
# last_digit = n % 10
# while n != 0:
#     first_digit = n % 10
#     quantity += 1
#     total *= first_digit
#     sum += first_digit
#     n = n // 10
# print(sum)
# print(quantity)
# print(total)
# print(sum/quantity)
# print(first_digit)
# print(first_digit+last_digit)

# Вторая цифра
# n = int(input())
# sec_digit = 0
# last_digit = n % 10
# while n > 9:
#     first_digit = n % 10
#     sec_digit = n % 10
#     n = n // 10
# print(sec_digit)

# Одинаковые цифры
# n = int(input())
# minn = 9
# maxx = 0
# # flag = True
# last_digit = n % 10
# while n !=0:
#     first_digit = n % 10
#     if first_digit < minn:
#      minn = first_digit
#     if first_digit > maxx:
#         maxx = first_digit
#     n = n // 10
# if minn == maxx:
#     print('YES')
# else:print('NO')

# n = int(input())
# flag = True
# last_digit = n % 10
# while n != 0:
#     first_digit = n % 10
#     if first_digit != last_digit:
#         flag = False
#     n = n // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# Упорядоченные цифры 🌶️
# n = int(input())
# flag = True
# last_digit = n % 10
# while n > 0:
#     if last_digit > n % 10:
#         flag = False
#     last_digit = n % 10
#     n //= 10

# if flag == True:
#     print('YES')
# else:
#     print('NO')

# 7.6
# Наименьший делитель
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0 and i != 1:
#         break
# print(i)

# Следуй правилам
# n = int(input())
# for i in range (1,n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

7.7
# count = 0
# p = 1
# for i in range(1,11):
#     x = int(input())
#     if x > -1:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# Ревью кода-3

# s = 0
# for i in range(1,8):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)

# Ревью кода-5 🌶️
# n = int(input())
# first = n % 10
# while n > 0:
#     last = n % 10
#     n //= 10
# print(last)

# Ревью кода-6
# n = int(input())
# total = 1
# last_digit = n % 10
# while n != 0:
#     first_digit = n % 10
#     total *= first_digit
#     n //= 10
# print(total)

# 7.8
# Таблица-1
# n = int(input())
# for i in range(1,n+1):
#     for j in range(3):
#         print(n,end=' ')
#     print()

# Таблица-2
# n = int(input())
# for i in range(1,n+1):
#     for j in range(5):
#         print(i,end=' ')
#     print()

# Таблица-3
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,10):
#         print(i,'+',j,'=',j+i,sep=' ')
#     print()

# Численный треугольник 1
# n = int(input())
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

# 12 месяцев
# total = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if n * 28 + k * 30 + m * 31 == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)

# Старинная задача
# rub = 0
# heads = 1
# for x in range(0,100):
#     for y in range(0,100):
#         for z in range(0,100):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 heads *= 1
#                 rub +=1
#                 print('bik =', x, 'korova =', y, 'pezduk =', z)
# print(rub, heads)

# 7.9
# Численный треугольник 2
# n = int(input())
# count = 0
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         count +=1
#         print(count,end=' ')
#     print()

# Численный треугольник 3
# n = int(input())
# for i in range (1,n+1):
#     for j in range(i):
#         print(j+1, end='')
#     for k in range(i-1,0,-1):
#             print(k,end='')
#     print()

# Делители-1 🌶️

# a, b = 1, 10
# # counter = 0 # счетчик подсчета суммы делителей
# number = 0 # число которое будем выводить (минимум 1)
# summa = 0  # тут будет сумма делителей, которую надо будет вывести
# for i in range(a, b + 1):  # проверяем каждое число в [a;b]
#     counter = 0 # обнуляем счетчик для каждого i
#     for j in range(1, i + 1):  # берем по очереди каждый делитель числа от [1 до самого числа]
#         if i % j == 0:  # если число делится на j без остатка, значит j - делитель числа
#             counter += j  # создаем сумму делителей
#     if counter >= summa:  # если сумма делителей больше или равна, чем суммаа делителей предыдущего числа
#         summa = counter  # то counter теперь равно кол-ву делителей этого числа вместо кол-ва предыдущего
#         number = i  # число у которого делителей оказалось больше, теперь равно number
# print(number, summa) # в конце концов, выводим само число (у которого больше делителей) и сумму этих делителей

# Делители-2
# n = int(input())
# for i in range (1,n+1):
#     counter = 0
#     for j in range (1,i+1):
#         if  i % j == 0:
#             counter += 1
#     print(i,'+'* counter ,sep='')
# print()
