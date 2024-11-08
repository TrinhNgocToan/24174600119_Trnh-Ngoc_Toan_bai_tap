so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
a = so1
b = so2
# Tìm ước chung lớn nhất bằng pp euclid
while b != 0:
  r = a % b
  a = b
  b = r
# Tính bội chung nhỏ nhất (BCNN)
ucln = a
bcnn = (so1 * so2) // ucln
print("Bội chung nhỏ nhất của là:", bcnn)