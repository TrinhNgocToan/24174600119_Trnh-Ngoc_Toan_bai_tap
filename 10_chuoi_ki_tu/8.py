str_1 = input("Nhập chuỗi thứ 1 của bạn vào đây : ").strip()
str_2 =  input("Nhập chuỗi thứ 2  của bạn vào đây : ").strip()
if str_2 in str_1 :
    print(f" Từ '{str_2}' nằm trong từ '{str_1}' ")
else :
    print(f" Từ '{str_2}' không nằm trong từ '{str_1}'")
if str_1 in str_2 :
    print(f" Từ '{str_1}' nằm trong từ '{str_2}'")
else :
    print(f" Từ '{str_1}' không nằm trong từ '{str_2}'")