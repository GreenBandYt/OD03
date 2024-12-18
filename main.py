import random
import timeit

# Генерируем большой массив из случайных чисел
array_size = 10000  # Размер массива
a = [random.randint(-1000, 1000) for _ in range(array_size)]

# Печатаем информацию о массиве
print(f"Был сгенерирован массив из {array_size} случайных чисел.")
print(f"Пример данных: {a[:10]} ... (выводим первые 10 элементов)")

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функция для измерения времени выполнения с использованием timeit
def measure_time_with_timeit(func, arr):
    return timeit.timeit(lambda: func(arr.copy()), number=1)

# Измеряем время для каждого алгоритма
print("\nРезультаты сортировок:")
print(f"Пузырьковая сортировка: {measure_time_with_timeit(bubble_sort, a):.6f} секунд")
print(f"Быстрая сортировка: {measure_time_with_timeit(quick_sort, a):.6f} секунд")
print(f"Сортировка выбором: {measure_time_with_timeit(selection_sort, a):.6f} секунд")
print(f"Сортировка вставками: {measure_time_with_timeit(insertion_sort, a):.6f} секунд")
