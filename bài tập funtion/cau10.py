def thap_phan_thanh_phan_so():
    so = float(input("Nhập vào một số thập phân: "))
    # Đếm số sau dấu phẩy để đổi thành phân số
    so_chu_so_thap_phan = len(str(so).split('.')[1]) if '.' in str(so) else 0
    mau_so = 10 ** so_chu_so_thap_phan  # Mẫu số là 10 mũ số chữ số thập phân
    # Chuyển đổi thành phân số tức là nhân ngược lên với 10 mũ ....
    tu_so = int(so * mau_so)  # Tử số là số thập phân nhân với mẫu số
    # Tìm ƯCLN của tử số và mẫu số
    def ucln(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    so_ucln = ucln(tu_so, mau_so)  # Tìm ƯCLN của tử số và mẫu số
    # Rút gọn phân số
    tu_so = tu_so // so_ucln
    mau_so = mau_so // so_ucln
    print(f"Phân số tương ứng với {so} là: {tu_so}/{mau_so}")

thap_phan_thanh_phan_so()
