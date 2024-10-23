import math

input_r = float(input("nhập bán kính của mặt đáy:"))
input_h = float(input("nhập chiều cao của khối trụ:"))

if input_r < 0 or input_h < 0:
    print("bán kính hoặc chiều cao không được âm")
else:
    pi = 3,14
    sxq = 2 * pi * input_r * input_h
    stp = sxq + (2 * pi * (input_r)**2)
    thetich = pi * (input_r ** 2) * input_h
    print(f"diện tích xung quanh là: {sxq:.2f}")
    print(f"diện tích toàn phần là: {stp:.2f}")
    print(f"thể tích là: {thetich:.2f}")