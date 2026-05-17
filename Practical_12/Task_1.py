n = int(input("Введите число n (n>=1): "))

odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]

print(f"Список нечётных чисел от 1 до {n}: {odd_numbers}")