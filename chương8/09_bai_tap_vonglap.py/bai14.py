#Viết chương trình vẽ tam giác Pascal và tam giác Floyd
# Nhập số hàng cho Tam giác Floyd
n = int(input("Nhập số hàng cho Tam giác Floyd: "))
a = 1
# Vẽ Tam giác Floyd
for i in range(1, n + 1):
    for j in range(i):
        print(a, end=' ')
        a += 1
    print()
print("\nTam giác Pascal:")
for i in range(n):
    # In khoảng trắng để tạo hình tam giác
    print(' ' * (n - i - 1), end='')
    b = 1
    for j in range(i + 1):
        # In giá trị của Tam giác Pascalb
        print(b, end=' ')
        # Tính giá trị tiếp theo của Tam giác Pascal
        b = b * (i - j) // (j + 1)
    
    print()
