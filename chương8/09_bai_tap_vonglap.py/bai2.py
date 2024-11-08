#S1 = 1 + 2 + 3 + 4 + …. + n
#S2 = 1*2*3*4*…*(n-1)
#S3 = 1 – 1/2 + 1/3 – 1/4 + …. + ((-1)**n)/n
#S4 tính tổng xích ma
n = int(input("Nhập số n là: "))
#Tính tổng s_1
if n > 0 :
    S_1 = 0 
    for i in range(n + 1) :
        S_1 += i 
    print(f"Giá trị của S_1 là :{S_1}")
#Tính tích S_2 
    S_2 = 1 
    for a in range(1,n+ 1) :
        S_2 *= a 
    print(f"Giá trị của S_2 là :{S_2}")
#Tính S_3 
    S_3 = 0 
    for c in range(1,n +1 ) :
        S_3 += ((-1)** (c + 1 )) / c
    print(f"Giá trị của S_3 là : {S_3:.2f}")
#Tính tổng xích ma của S_4:
    S_4 = 0 
    for k in range(n + 1):
        S_4 = k / (k + 2 )
    print(f"Giá trị của S_4 là : {S_4:.4f}")
else :
    print("Bạn đã nhập sai điều kiện của đề bài ")