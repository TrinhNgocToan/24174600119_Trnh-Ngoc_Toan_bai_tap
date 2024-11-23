nhap_chuoi = input("Nhập chuỗi bất kì của bạn vào đây :")
chu_viet_hoa = 0 
chu_viet_thuong = 0 
for chu in nhap_chuoi :
    if chu.isupper() :
        chu_viet_hoa +=1 
    elif chu.islower() :
        chu_viet_thuong += 1 
print(f"Số từ viết hoa là :{chu_viet_hoa}")
print(f"Số từ viết thường  là :{chu_viet_thuong}")