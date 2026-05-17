# Вводим лабиринт (25 символов)
maze = input("Введите строку лабиринта (25 символов): ")

# 1.1 — Выводим лабиринт построчно (5 строк по 5 символов)
print("\nЛабиринт:")
print(maze[0:5])
print(maze[5:10])
print(maze[10:15])
print(maze[15:20])
print(maze[20:25])

# 1.2 — Находим вход («н»)
start_index = maze.find('н')
start_row = start_index // 5  # номер строки (0–4)
start_col = start_index % 5   # номер столбца (0–4)
print(f"Вход: строка {start_row}, столбец {start_col}")

# 1.3 — Находим выход («ф»)
exit_index = maze.find('ф')
exit_row = exit_index // 5
exit_col = exit_index % 5
print(f"Выход: строка {exit_row}, столбец {exit_col}")


# 1.4 — Считаем Манхэттенское расстояние
distance = abs(start_row - exit_row) + abs(start_col - exit_col)
print(f"Расстояние между входом и выходом: {distance} шагов")
