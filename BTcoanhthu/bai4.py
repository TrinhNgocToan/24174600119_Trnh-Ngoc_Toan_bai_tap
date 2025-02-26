# Nhập ba số
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
so3 = float(input("Nhập số thứ ba: "))
# Tìm số lớn nhất
smax = so1  # Giả sử số 1 là lớn nhất
if so2 >= smax:
    smax = so2
if so3 >= smax:
    smax = so3
# In kết quả
print("Số lớn nhất trong ba số là:", smax)