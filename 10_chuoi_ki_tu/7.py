chuoi = input("Nhập chuỗi bạn muốn kiểm tra :")
if chuoi.count('.') == 1 and chuoi.replace('.','').isdigit():
    print("Đây là số thập phân ")
else :
    print("Đây ko phải số thập phân ")