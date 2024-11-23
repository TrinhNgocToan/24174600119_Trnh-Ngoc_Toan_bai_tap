ho_ten = input("Nhập họ tên đầy đủ: ").strip()
danh_sach_ten = ho_ten.split()
ho = danh_sach_ten[0] 
ten = danh_sach_ten[-1]  
print("Họ:", ho)
print("Tên:", ten)
