# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1

#     num = num // 10

# print(total)

# Обратный порядок 1

# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     print(last_digit)
#     n = n // 10

# Обратный порядок 2

# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     print(last_digit, end='')
#     n = n // 10

# max и min
# n = int(input())
# maax = 0
# miin = 9
# while n > 0:
#      last_digit = n % 10
#      if last_digit > maax:
#           maax = last_digit
#      if last_digit < miin:
#           miin = last_digit
#      n //= 10
# print('Максимальная цифра равна',maax)
# print('Минимальная цифра равна',miin)


# Все вместе

# n = int(input())
# count = 0
# total = 0
# product = 1
# l_digit = n % 10
# while n !=0:
#     last_digit = n % 10
#     total += last_digit
#     product *= last_digit
#     count += 1
#     first_digit = n 
#     n = n // 10
# print(total)
# print(count)
# print(product)
# print(total/count)
# print(first_digit)
# print(first_digit+l_digit)

# Вторая цифра
# n = int(input())
# while n > 9:
#     digit = n % 10
#     n = n //10
# print(digit)

# Одинаковые цифры
# n = int(input())
# last_digit = n % 10
# flag = True
# while n != 0:
#     last2 =n % 10
#     if last_digit != last2:
#         flag = False
#     n = n //10
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# Упорядоченные цифры 🌶️
# n = int(input())
# flag = True
# while n >= 10:
#     last =n % 10
#     prlast = n % 100 // 10
#     if last > prlast:
#         flag = False
#     n = n //10
# if flag == True:
#     print('YES')
# else:
#     print('NO')
