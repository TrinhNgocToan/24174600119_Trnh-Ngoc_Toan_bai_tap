luong = float(input("Nhập lương nhân viên (đồng): "))
# Tính thuế thu nhập
if luong > 15000000:
    thue = luong * 0.3
elif 7000000 <=luong <= 15000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1
# Tính lương ròng
luong_rong = luong - thue
print(f"Thuế thu nhập: {thue:.2f} đồng")
print(f"Lương ròng (số tiền thực nhận): {luong_rong:.2f} đồng")