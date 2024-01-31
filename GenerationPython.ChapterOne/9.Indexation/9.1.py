# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# В столбик 1.
# n = input()
# for i in range(0,len(n),2):
#     print(n[i])

# В столбик 2
# n = input()
# for i in range(-1,-len(n)-1,-1):
#     print(n[i])

# ФИО
# a,b,c = input(),input(),input()
# print(b[0],a[0],c[0],sep='')

# Цифра 1
# n = input()
# total = 0
# for i in range (0,len(n)):
#     total +=int(n[i]) 
# print(total)

# Цифра 2
# n = input()
# success = True
# for i in range(len(n)):
#     if n[i] in '0123456789':
#         print('Цифра')
#         success = False
#         break
# if success:
#     print('Цифр нет')
   
# Сколько раз?  

# n = input()
# counter = 0
# counter1 = 0
# for i in range(len(n)):
#     if '+' in n[i]:
#         counter +=1
#     if '*' in n[i]:
#         counter1 +=1
# print('Символ + встречается',counter, 'раз')
# print('Символ * встречается',counter1, 'раз')
      
# Одинаковые соседи
# n = input()
# flag = True
# counter = 0
# for i in range (len(n)-1):
#     if n[i] == n[i+1]:
#         counter += 1
# print(counter)

# Гласные и согласные
# n = input()
# counterG = 0
# counterS = 0
# for i in range(len(n)):
#     if n[i] in 'АЯУЮОЕЭИЫаяуюоеэиы':
#         counterG += 1
#     if n [i] in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ':
#         counterS += 1
# print('Количество гласных букв равно',counterG)
# print('Количество согласных букв равно',counterS)

# Decimal to Binary
# n = int(input())
# s = ''
# s2 = ''
# while n >0:
#     s += str(n%2)
#     n //= 2
# for i in range (-1,-len(s)-1, -1):
#     s2 += s[i]
# print(s2)