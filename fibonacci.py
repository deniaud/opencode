# Простой код для вывода 10 первых чисел Фибоначчи

def fibonacci(n):
    """Генерирует первые n чисел Фибоначчи"""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Выводим 10 первых чисел Фибоначчи
result = fibonacci(10)
print("Первые 10 чисел Фибоначчи:")
print(result)
