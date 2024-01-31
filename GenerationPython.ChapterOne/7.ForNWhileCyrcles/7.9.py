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
# num = int(input())
# while num >9:
#     Sum 