import numpy as np
import math

data_steps = np.array([
    8200, 11500, 9400, 7100, 10800, 8600, 12900, 45000, 9900, 9100,
    7600, 11300, 8300, 9700, 10400, 8900, 12100, 6800, 10200, 9200,
    200, 450, 8100, 11600, 7900, 9600, 10700, 8700, 12200, 6900
])
sort_steps = np.sort(data_steps)
sum_step = 0

# count = sum(i for i in data_steps)
# print(f"Среднее кол-во шагов: {count/len(data_steps)}")
middle_steps = np.mean(data_steps)
print(f"Среднее кол-во шагов: {middle_steps}")

# count_steps = len(data_steps)
# if (count_steps % 2 == 0):
#     num_median = (count_steps/2)
#     meddian_1 = sort_steps[int(num_median)]
#     meddian_2 = sort_steps[int(num_median)-1]
#     meddian = (meddian_1+meddian_2)/2
#     print(f"Медиан - {meddian}")
# else:
#     num_median = (count_steps/2)
#     meddian = sort_steps[int(num_median)]
#     print(f"Медиан - {meddian}")
print(f"Медиан - {np.median(data_steps)}")

# for i in data_steps:
#     a = i - middle_steps
#     sum_step += a**2
# print("Стандартное отклонение: " + str(math.sqrt(sum_step/len(data_steps))))
print("Стандартное отклонение: " + str(np.std(data_steps)))

# for i in data_steps:
#     a = i - middle_steps
#     sum_step += a**2
# print("Дисперсия: " + str(sum_step/len(data_steps)))
print("Дисперсия: " + str(np.var(data_steps)))

# min = data_steps[0]
# for i in data_steps:
#     if (i < min):
#         min = i
# print("Минимальное значение: " + str(min))
# max = data_steps[0]
# for i in data_steps:
#     if i > max:
#         max = i
# print("Максимальное значение: " + str(max))
print("Минимальное значение: " + str(np.min(data_steps)))
print("Максимальное значение: " + str(np.max(data_steps)))

# min = data_steps[0]
# for i in data_steps:
#     if (i < min):
#         min = i
# max = data_steps[0]
# for i in data_steps:
#     if i > max:
#         max = i
# print("Размах данных " + str(max-min))
print("Размах данных " + str(np.ptp(data_steps)))


print("Перцентель 25 " + str(np.percentile(sort_steps, 25)))
print("Перцентель 50 " + str(np.percentile(sort_steps, 50)))
print("Перцентель 75 " + str(np.percentile(sort_steps, 75)))
print("Перцентель 90 " + str(np.percentile(sort_steps, 90)))
print("Перцентель 99 " + str(np.percentile(sort_steps, 99)))

print("Первый квартиль: " + str(np.percentile(sort_steps, 25)))
print("Третий квартиль: "  + str(np.percentile(data_steps, 75)))



# IQR = 0
# Q1 = (len(data_steps)-1)*(0.25)
# Q3 = (len(data_steps)-1)*(0.75) 
# if (len(data_steps) % 2 == 0):
#     step_Q3 = (sort_steps[int(Q3)] + sort_steps[int(Q3)+1])/2
#     step_Q1 = (sort_steps[int(Q1)] + sort_steps[int(Q1)+1])/2
#     IQR = step_Q3-step_Q1
# else:
#     IQR = sort_steps[int(Q3)] - sort_steps[int(Q1)]

# print("Межквартальный размах: " + str(IQR))
print("Межквартальный размах: " + str(np.percentile(sort_steps, 75) - np.percentile(sort_steps, 25)))

IQR = np.percentile(sort_steps, 75) - np.percentile(sort_steps, 25)
low_border = np.percentile(sort_steps, 25) - 1.5*IQR
high_border = np.percentile(sort_steps, 75) + 1.5*IQR
print("Нижняя граница: " + str(low_border))
print("Верхняя граница: " + str(high_border))
print("Выбросы: ")
for i in sort_steps:
    if i < low_border or high_border < i:
        print(i)

print()

A = np.array([8000, 12000, 9500, 7000, 11000, 8500, 13000, 6000, 10000, 9000, 7500, 11500, 8200, 9800, 10500])
print("Матрица:")
matrix = A.reshape(3,5)
print(matrix)
print("Размерность матрицы:")
print(matrix.shape)

(n, m) = matrix.shape
sum = 0
# for i in range(0, n):
#     for q in range(0, m):
#         sum += matrix[i, q]
# print("Сумма всех элементов матрицы:")
# print(sum) 
print("Сумма всех элементов матрицы:")
print(np.sum(matrix))

print("Сумма по столбцам:")
# for i in range(0, m):
#     sum = 0
#     for q in range(0, n):
#         sum += matrix[q, i]
#     print(f"Столбец №{i+1}: {sum}")
print(np.sum(matrix, axis=0))

print("Сумма по строкам")
# for i in range(0, n):
#     sum = 0
#     for q in range(0, m):
#         sum += matrix[i, q]
#     print(f"Строка №{i+1}: {sum}")
print(np.sum(matrix, axis=1))

print("Транспонирование матрицы:")
matrixT = matrix.T
print(matrixT)

print("Среднее значение матрицы: " + str(np.mean(matrix)))
print("Стандартное отклонение: " + str(np.std(matrix)))
print("Дисперсия: " + str(np.var(matrix)))
print("Первый квартиль: " + str(np.percentile(matrix, 25)))
print("Второй квартиль: " + str(np.percentile(matrixT, 50)))
print("Третий квартиль: " + str(np.percentile(matrixT, 75)))

print("Индивидульный вопрос:")
for i in data_steps:
    if i < 8000:
        print(i)