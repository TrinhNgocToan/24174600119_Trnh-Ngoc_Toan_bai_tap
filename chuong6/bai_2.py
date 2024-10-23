import math

# nhập giá trị cho x
x = float(input("Nhập giá trị của x: "))
phan_tu = -x + math.sqrt(x**2 + 4)
phan_mau = (x**4 + 1) ** (1/7)
ket_qua = (phan_tu / phan_mau)
# in ra kết quả
print(f"Giá trị của f(x): {ket_qua:.2f}")