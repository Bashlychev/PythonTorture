# Ревью кода - 7 🌶️

# n = int(input())
# s = 0
# # last_digit = n % 10
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# Ревью кода - 8 🌶️
# n = 8
# count = 0
# maximum = -10 ** 12
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# Третья цифра
# n = int(input())
# third = 0
# last_digit = n % 10
# while n > 99:
#     first_digit = n % 10
#     third = n % 10
#     n //= 10
# print(third)

# Звездная рамка
# n = int(input())
# print('*'*19)
# for i in range (1,n-1):
#     print('*','*',sep='                 ')
# print('*'*19)

# Все вместе 2
# n = int(input())
# count3 = 0
# lastdig = 0
# chentiy = 0
# sumbol5 = 0
# proizbol7 = 1
# sum0and5 = 0
# last_digit = n % 10
# while n != 0:
#     first_digit = n % 10
#     if first_digit == 3:
#         count3 += 1
#     if first_digit == last_digit:
#         lastdig += 1
#     if n % 2 == 0:
#         chentiy += 1
#     if first_digit >= 6:
#         sumbol5 += first_digit
#     if first_digit >= 8:
#         proizbol7 *= first_digit
#     if first_digit == 0 or first_digit == 5:
#         sum0and5 += 1
#     n = n // 10
# print(count3)
# print(lastdig)
# print(chentiy)
# print(sumbol5)
# print(proizbol7)
# print(sum0and5)
    
#     Ревью кода - 9
#     n = 4
# count = 0
# maximum = -(10 ** 4)
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

