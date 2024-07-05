numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# Проверка каждого числа из списка numbers
for a in numbers:
    # Инициализация флага
    is_prime = True

    # Проверка делителей от 2 до квадратного корня (деления на самого себя)
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            is_prime = False
            break  # Оптимизация с помощью break

    # Добавление числа в соответствующий список
    if is_prime:
        primes.append(a)
    else:
        not_primes.append(a)

# Печать результатов
print(f"Список простых чисел: {primes}")
print(f"Список не простых чисел: {not_primes}")
