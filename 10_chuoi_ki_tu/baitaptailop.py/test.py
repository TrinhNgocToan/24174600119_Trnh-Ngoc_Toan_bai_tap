def ktrasonguyenduong():
    n = input("Nhập vào n: ")
    if n.isdigit():  # Kiểm tra n chỉ chứa các chữ số
        n = int(n)   # Chuyển n sang kiểu số nguyên
        if n > 0:
            print("Đây là số nguyên dương.")
        else:
            print("Đây không phải là số nguyên dương (bằng 0 hoặc âm).")
    else:
        print("Đây không phải là số nguyên.")


ktrasonguyenduong()
