# Nhập lựa chọn chuyển đổi
print("Chọn kiểu chuyển đổi:")
print("1. Chuyển từ cơ số 10 sang cơ số 2")
print("2. Chuyển từ cơ số 2 sang cơ số 10")
chon = int(input("Nhập lựa chọn (1 hoặc 2): "))
if chon == 1:
    # Chuyển từ cơ số 10 sang cơ số 2
    n = int(input("Nhập số trong hệ cơ số 10: "))
    if n == 0:
        print("0 trong hệ cơ số 10 là: 0 trong hệ cơ số 2.")
    else:
        he2 = ""
        while n > 0:
            he2 = str(n % 2) + he2  # Lấy phần dư và cộng vào kết quả
            n = n // 2  # Chia cho 2
        print(f"{n} trong hệ cơ số 10 là: {he2} trong hệ cơ số 2.")
elif chon == 2:
    # Chuyển từ cơ số 2 sang cơ số 10
    he2 = input("Nhập số trong hệ cơ số 2: ")
    # Kiểm tra đầu vào có phải là nhị phân không (chỉ chứa '0' và '1')
    if all(bit in '01' for bit in he2):
        he10 = 0
        # Duyệt qua từng ký tự trong chuỗi nhị phân
        for i in range(len(he2)):
            he10 += int(he2[-(i + 1)]) * (2 ** i)  # Tính giá trị thập phân từ nhị phân
        print(f"{he2} trong hệ cơ số 2 là: {he10} trong hệ cơ số 10.")
    else:
        print("Đầu vào không phải là số nhị phân hợp lệ.")
else:
    print("Lựa chọn không hợp lệ.")