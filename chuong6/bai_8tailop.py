import math
# nhập các con điểm
diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kì: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kì: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
# xếp loại
if diem_trung_binh >= 9:
    print("điểm của bạn thuộc loại A")
elif diem_trung_binh >= 7 and diem_trung_binh <= 9:
    print("điểm của bạn thuộc loại B")
elif diem_trung_binh >= 5 and diem_trung_binh <= 7:
    print("điểm của bạn thuộc loại C")
else:
    print("điểm của bạn thuộc loại D")
    