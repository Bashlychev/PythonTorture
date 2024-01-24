# # Оператор прерывания цикла break
# # num = int(input())
# # flag = True

# # for i in range(2, num):
# #     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
# #         flag = False
# #         break               # останавливаем цикл если встретили делитель числа        

# # if flag:  # эквивалентно if flag == True:
# #     print('Число простое')
# # else:
# #     print('Число составное')


# Напишем программу, использующую цикл for, которая считывает 10 чисел и суммирует их до тех пор, пока не обнаружит отрицательное число

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# Напишем программу, которая определяет, содержит ли введенное пользователем число цифру 7.

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10

# if flag:  # эквивалентно if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# for i in range(10):
#     print(i, end="*")
#     if i > 6:
#         break


# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)


# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# Наименьший делитель
# n = int(input())

# for i in range (2,n+1):
#     if n % i == 0 and i >1:
#         break
# print(i)

# Следуй правилам

# n = int(input())
# for i in range (1,n+1):
#     if i in range(5,10) or i in range(17,38) or i in range(78,88):
#         continue
#     print(i)

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Цикл завершен.')

# num = int(input())
# n = num
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', num, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', num, 'не содержит цифру 7')
