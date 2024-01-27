# # Таблица-1
# # n = int(input())
# # for i in range(n):
# #     for y in range(3):
# #         print(n,end=' ')
# #     print()    


# # Таблица-2
# # n = int(input())
# # for i in range(1,n+1):
# #     for _ in range(5):
# #         print(i,end=' ')
# #     print()
        
# # Таблица-3
# # n = int(input())
# # for i in range(1,n+1):
# #     for j in range(9):
# #         print(i,'+',j+1,'=',i+j+1,sep=' ')
# #     print()

# # # Звездный треугольник 🌶️🌶️
# # n = int(input())
# # for i in range(1, n // 2 + 2):
# #     print('*' * i)
# # for j in range(n // 2, 0, -1):
# #     print('*' * j)

# # Численный треугольник 1
# n = int(input())
# for i in range (1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()

# 12 месяцев
# total = 0
# for n in range(1, 13):
#     for k in range(1, 12): 
#         for m in range(1,12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =',m)
# print('Общее количество натуральных решений =', total)

# Старинная задача
# total = 0
# for x in range(0, 100):
#     for y in range(0, 100):
#         for z in range(0,100):
#             if 10 * x + 5 * y + 0.5 * z == 100 and x + y + z == 100:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# Гипотеза Эйлера о сумме степеней 🌶️🌶️
# total = 0
# for a in range(1, 5):
#     for b in range(1, 2): 
#         for c in range(1,1):
#             for d in range (1,1):
#                 if 27 * a + 84 * b + 110 * c + 133 * d  == 144:
#                     total += 1
#                     print('a =', a, 'b =', b, 'c =',c, 'd =',d)
# print('Общее количество натуральных решений =', total)

# for a in range(1, 150):
#     for b in range(1, 150):
#         for c in range(1, 150):
#             for d in range(1, 150):
#                 for e in range(1, 150):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a + b + c + d + e)