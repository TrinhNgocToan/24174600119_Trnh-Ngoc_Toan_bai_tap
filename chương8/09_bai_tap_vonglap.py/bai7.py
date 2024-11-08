#Viết chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n
n = int(input("Nhập số cần kiểm tra: "))
# so nguyen to phai lon hon 1
for z in range(2, n):
    so_chia = z
    #so bi chia phai lon hon 1 va nho hon so chia(dk de la so nguyen to)
    for i in range(2, so_chia):
        if (so_chia % i == 0 and so_chia != i):
            #print(f"{z} không phải là số nguyên tô.")
            break
    else:
        print(f"{z} là số nguyên tố.")