m = int(input("nhập vào tháng bạn muốn ktra:"))
y = int(input("nhập vào năm bạn muốn ktra:"))
if m > 0 and m < 13 and y >0:
    if y % 4 ==0:
        if m == 2:
            print(f" tháng 2 có 29 ngày")
        elif m == 1 or m==3 or m == 5 or m ==7 or m == 8 or m == 10 or m == 12:
            print(f" tháng {m} có 31 ngày")
        else:
            print(f"tháng {m} có 30 ngày")
    if y % 4 !=0:
        if m == 2:
            print(f" tháng 2 có 28 ngày")
        elif m == 1 or m==3 or m == 5 or m ==7 or m == 8 or m == 10 or m == 12:
            print(f" tháng {m} có 31 ngày")
        else:
            print(f"tháng {m} có 30 ngày")
else:
    print("hãy nhập lại năm và tháng cho đúng")