print("Only even numbers")

all_even = True

for i in range(11):
    num = int(input("Введте число: "))
    if num % 2 == 0:
        all_even = False
if all_even:
    print("YES")
else:
    print("NO")

