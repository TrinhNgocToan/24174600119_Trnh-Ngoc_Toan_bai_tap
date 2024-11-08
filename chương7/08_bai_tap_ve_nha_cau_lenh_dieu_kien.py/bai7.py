print("ta có ma trận như sau")
print("a1   b1   c1")
print("a2   b2   c2")
print("tương ứng với")
print("a_1*x + b_1*y = c_1")
print("a_2*x + b_2*y = c_2")
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))
# Tính định thức D
D = a1 * b2 - a2 * b1
if D == 0:
    # Kiểm tra trường hợp vô số nghiệm hoặc không có nghiệm
    D1 = c1 * b2 - c2 * b1
    D2 = a1 * c2 - a2 * c1
    if D1 == 0 and D2 == 0:
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
else:
    # Tính nghiệm x và y theo công thức Cramer
    x = (c1 * b2 - c2 * b1) / D
    y = (a1 * c2 - a2 * c1) / D
    print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")