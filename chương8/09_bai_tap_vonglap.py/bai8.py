n = int(input("Nhập vào số nguyên n: "))
so_luong= 0
# Tìm các số hoàn hảo nhỏ hơn n
for num in range(1, n):
    tong = 0
    for i in range(1, num):
        if num % i == 0:
            tong += i
    if tong == num:
        print(f"Số hoàn hảo: {num}")
        so_luong += 1
# In ra thông báo nếu không tìm thấy số hoàn hảo
if so_luong == 0:
    print(f"Không có số hoàn hảo nào nhỏ hơn {n}.")