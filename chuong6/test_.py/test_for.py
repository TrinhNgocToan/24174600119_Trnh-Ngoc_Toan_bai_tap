n = int(input("Nhập số hàng cho Tam giác Floyd: "))
a = 1
# Vẽ Tam giác Floyd
for i in range(1, n + 1):
    for j in range(i):
        print(a, end=' ')
        a += 1
    print()
print("\nTam giác Pascal:")
