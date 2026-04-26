n = int(input("Введите n (n ≥ 2): "))
max1 = float()  # первое наибольшее
max2 = float()  # второе наибольшее

for i in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)