import math
gia_tien_dien = 7000
U = 220 
I = 2.7 
t = float(input("Thời gian sử dụng điện là: "))

if t <= 0 :
    print("thời gian sử dụng điện không thể bé hơn hoặc bằng 0:")
else :
    P = U * I
    # Lượng điện tiêu thụ là
    W = P * t / 3600 * 1000  #kwh
    # Tiền điện phải trả là 
    tien_dien = W * gia_tien_dien
    print(f"TIỀN ĐIỆN CỦA BẠN LÀ: {tien_dien:2f} ")