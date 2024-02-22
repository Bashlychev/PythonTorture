# Численный треугольник 2
# n = int(input())
# counter = 1
# for i in range(1,n+1):
#     for y in range(1,i+1):
#         print((counter),end=' ')
#         counter += 1
#     print() 
   
# Численный треугольник 3
# n = int(input())
# for i in range(1,n+1):
#     for y in range(1,i+1):
#         print(y,end='')
#     for k in range (i-1,0,-1):
#         print(k,end='') 
#     print()  
    
# Делители-1 🌶️
# a = int(input())
# b = int(input())
# total = 0
# max_total = 0
# x = 0
# for i in range (a,b+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             total += j
#     if total >= max_total:
#         max_total = total
#         x = i
#     total = 0
# print(x, max_total)

# Делители-2
# n = int(input())
# counter = 0
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             counter +=1
#     print(str(i) + '+' * counter)
#     counter = 0

# Цифровой корень
# n = 
# sum1 = 0
# sum2 = 0
# last_digit = n % 10
# for i in range(1,n+1):
#     first_digit = n % 10
#     sum1 += first_digit
#     n //= 10
# last_digit2 = n % 10
# for j in range(1,sum1+1):
#     first_digit2 = sum1 % 10
#     sum2 += first_digit2
#     sum1 //= 10
# print(sum2)

# Цифровой корень
# n = int(input())
# while n > 9:
#     total = 0
#     while n > 0:
#         last_digit = n % 10
#         total += last_digit
#         n //= 10
#     n = total
# print(n)

# Сумма факториалов

# from math import *
# n = int(input())
# fact = 0
# for i in range(1,n+1):
#     fact +=factorial(i)
# print(fact)

# Простые числа
# a,b = int(input()),int(input())
# count = 0
# for i in range (a,b+1):
#     for j in range (1,i+1):
#         if i % j == 0:
#             count +=1
#     if count == 2:
#         print(i)
#     count = 0

        

