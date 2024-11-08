so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
a = so1
b = so2
# Thuật toán Euclid
while b != 0:
    r = a % b
    a = b
    b = r
print("Ước chung lớn nhất của là ",a)