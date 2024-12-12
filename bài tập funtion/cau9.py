def toi_gian_phan_so():
    a = int(input("Nhập tử số: "))
    b = int(input("Nhập mẫu số: "))
    # xây dựng hàm trong hàm
    def ucln(x, y):
        while y != 0: #thuật toán tìm ucln euclid
            x, y = y, x % y
        return x
    # Tìm ƯCLN của tử số và mẫu số
    so_ucln = ucln(a, b)
    #rút gọn
    a = a // so_ucln
    b = b // so_ucln
    print(f"Phân số sau khi rút gọn là: {a}/{b}")


toi_gian_phan_so()
