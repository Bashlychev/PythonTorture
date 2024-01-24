# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# Ревью кода-1 🌶️🌶️
# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# Ревью кода-2 🌶️🌶️
# mx = -1000000000000
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s ==0:
#     print('NO')
# else:
#     print(s)
#     print(mx)

# Ревью кода-3
# count = 0
# for _ in range(1,8):
#     n = int(input())
#     if n % 2 == 0:
#         count = count + n
# print(count)

# Ревью кода-4 🌶️🌶️
n = int(input())
max_digit = -1
min_digit = 9
while n > 0:
    last_digit = n % 10
    if last_digit % 3 == 0:
        max_digit = last_digit
    if last_digit < max_digit:
        min_digit = last_digit
    n //=10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)

# Ревью кода-5 🌶️
# n = int(input())
# while n > 0:
#     first_digit = n
#     n //= 10
# print(first_digit)

# Ревью кода-6
# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)
