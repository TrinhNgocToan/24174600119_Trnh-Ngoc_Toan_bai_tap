def tinh_tong_day_so():
    day_so = input("Nhập dãy số nguyên, cách nhau bởi dấu phẩy: ")
    cac_so = list(map(int, day_so.split(',')))
    tong = 0  
    for so in cac_so:
        tong += so 
    print(f"Tổng của dãy số là: {tong}")

tinh_tong_day_so()
