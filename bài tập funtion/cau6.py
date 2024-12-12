def ktrasochinhphuong():
    n = input("Nhập vào một số: ")
    if n.isdigit():  
        sqrt_n = int(n ** 0.5)  
        if sqrt_n * sqrt_n == n:  
            print(f"{n} là số chính phương.")
        else:
            print(f"{n} không phải là số chính phương.")
    else:
        print("Vui lòng nhập một số nguyên dương.")

ktrasochinhphuong()
