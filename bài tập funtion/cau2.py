def ktrasonguyenduong():
    n = input("Nhập vào n: ")
    if n.isdigit():  
        n = int(n)  
        if n > 0:
            print("Đây là số nguyên dương.")
        else:
            print("Đây không phải là số nguyên dương")
    else:
        print("Đây không phải là số nguyên.")

ktrasonguyenduong()
