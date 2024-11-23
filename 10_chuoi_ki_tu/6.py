chuoi = input("Nhập số bạn muốn kiểm tra :")
if  len(chuoi) > 1 and chuoi[0] == "-" and chuoi[1:].isdigit() :                                       
    print("ĐÂY là chuỗi kí tự âm ")
else :
    print("Đây ko phải là chuỗi kí tự âm ")