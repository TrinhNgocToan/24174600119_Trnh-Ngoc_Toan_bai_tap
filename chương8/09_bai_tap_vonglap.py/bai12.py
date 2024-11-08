tu_so = int(input("nhập vào tử số"))
mau_so= int(input("nhập vào mẫu số"))
if mau_so==0:
    print("mẫu số không thể bằng không")
else :
    a= tu_so
    b= mau_so
    while b!=0:
        r = a%b
        a=b
        b=r
    ucln=a
    tu_so_toi_gian = tu_so/ucln
    mau_so_toi_gian= mau_so/ucln
    print("Phân số tối giản là:", tu_so_toi_gian, "/", mau_so_toi_gian)