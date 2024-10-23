import math 
x = float(input("Nhập giá trị x: "))
if x < 0:
    print ("hệ số không được âm:")
else:
    f = math.log(4,x) + math.log(x,2)
    print(f"Giá trị của f là: { f:4.2f}")