# В столбик 1
# a = 'abcdefghijklmnop'
# for i in range(0,len(a),2):
#     print(a[i],sep='')

# В столбик 2
# a = 'abc'
# for i in range (-1,-len(a)-1,-1):
#     print(a[i],sep='')

# # ФИО
# a,b,c = input(),input(),input()
# print(b[0],a[0],c[0],sep='')

# Цифра 1
# s = '2514'
# sum = 0
# for i in range (0,len(s)):
#     sum += int(s[i])
# print(sum)

# n = 12345
# sum = 0
# last_digit = n % 10
# while n != 0:
#     first_digit = n % 10
#     sum += first_digit
#     n //= 10
# print(sum)

# Цифра 2
# a = input()
# flag = True
# for i in range (len(a)):
#     if a[i] in '0123456789':
#         flag = False
#         break
       
# if flag == False:
#     print('Цифра')
# else:
#     print('Цифр нет')

# Сколько раз?
# a = input()
# plus = 0
# star = 0
# for i in range (len(a)):
#     if a[i] == '*':
#         star += 1
#     if a [i] == '+':
#         plus += 1
# print('Символ','+','встречается',plus,'раз')
# print('Символ','*','встречается',star,'раз')

# Одинаковые соседи
# a = input()
# sum = 0
# for i in range(len(a)-1):
#     if a[i] == a[i+1]:
#         sum += 1
# print(sum)

# Гласные и согласные
# a = input()
# glas = 0
# sogl = 0
# for i in range(len(a)):
#     if a[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         sogl += 1
#     if a[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         glas += 1
# print('Количество гласных букв равно',glas)
# print('Количество согласных букв равно',sogl)