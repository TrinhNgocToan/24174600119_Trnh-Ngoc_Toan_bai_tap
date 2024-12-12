def ktrasonguyento():
    n = input("Nhập vào một số: ")
    if n.isdigit():  
        n = int(n)
        if n < 2: #số ngto phải lớn hơn 2
            print("n không phải là số nguyên tố.")
        else:
            so_ngto = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:  # Nếu n chia hết cho i
                    so_ngto = False
                    break
            if so_ngto:
                print("n là số nguyên tố.")
            else:
                print("n không phải là số nguyên tố.")
    else:
        print("Vui lòng nhập một số nguyên dương.")

# Gọi hàm để kiểm tra
ktrasonguyento()
