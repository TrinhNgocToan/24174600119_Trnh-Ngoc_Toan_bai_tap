def tinh_tich_day_so():
    day_so = input("Nhập dãy số nguyên, cách nhau bởi dấu phẩy: ")
    cac_so = list(map(int, day_so.split(',')))
    tich = 1  
    for so in cac_so:
        tich *= so  
    print(f"Tích của dãy số là: {tich}")

tinh_tich_day_so()
