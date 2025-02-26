n = int(input("nhập số tháng bạn đã làm được:"))
if n <12 :
    luong = 1350000*2.34
elif n > 12 and n< 36:
    luong = 1350000*3.33
elif n > 36 and n < 60:
    luong = 1350000*3.66
else:
    luong = 1350000*3.99
print(luong)