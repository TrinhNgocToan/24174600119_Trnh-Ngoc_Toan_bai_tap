chuoi = input("Nhập chuôix của bạn vào đây :")
ki_tu_chu = 0 
ki_tu_so = 0 
ki_tu_dac_biet = 0 
for chu in chuoi :
    if chu.isalpha() == True :
        ki_tu_chu = ki_tu_chu + 1 
    else :
        if chu.isdigit() == True :
            ki_tu_so = ki_tu_so + 1 
        else :
            ki_tu_dac_biet = ki_tu_dac_biet + 1 
print(f"Số kí tự chữ là :{ki_tu_chu}")
print(f"Số kí tự số là :{ki_tu_so}")
print(f"Số kí tự đặc biệt là :{ki_tu_dac_biet}")