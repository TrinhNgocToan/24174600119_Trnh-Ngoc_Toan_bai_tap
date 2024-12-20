danh_sach_mat_hang = []

def xem_danh_sach_mat_hang():
    if not danh_sach_mat_hang:
        print("Danh sách mặt hàng trống.")
    else:
        print("\nDanh sách mặt hàng:")
        for hang in danh_sach_mat_hang:
            print(hang)

def nhap_thong_tin_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        
        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": 0.0,
            "vat": 0.0
        }
        danh_sach_mat_hang.append(mat_hang)
        print("Thêm mặt hàng thành công.")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho đơn giá và số lượng.")

def tinh_thanh_tien_va_vat():
    for hang in danh_sach_mat_hang:
        hang["thanh_tien"] = hang["don_gia"] * hang["so_luong"]
        hang["vat"] = hang["thanh_tien"] * 0.1
    print("Đã tính thành tiền và thuế VAT cho các mặt hàng.")

def xoa_mat_hang_theo_ma():
    try:
        ma_xoa = input("Nhập mã hàng cần xóa: ")
        for hang in danh_sach_mat_hang:
            if hang["ma_hang"] == ma_xoa:
                danh_sach_mat_hang.remove(hang)
                print("Xóa mặt hàng thành công.")
                return
        print("Không tìm thấy mặt hàng với mã đã nhập.")
    except Exception as e:
        print(f"Lỗi: {e}")

def chinh_sua_mat_hang_theo_ma():
    try:
        ma_sua = input("Nhập mã hàng cần chỉnh sửa: ")
        for hang in danh_sach_mat_hang:
            if hang["ma_hang"] == ma_sua:
                print("Mặt hàng hiện tại:", hang)
                hang["ten_hang"] = input("Nhập tên hàng mới: ")
                hang["don_vi_tinh"] = input("Nhập đơn vị tính mới: ")
                hang["don_gia"] = float(input("Nhập đơn giá mới: "))
                hang["so_luong"] = int(input("Nhập số lượng mới: "))
                print("Chỉnh sửa mặt hàng thành công.")
                return
        print("Không tìm thấy mặt hàng với mã đã nhập.")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho đơn giá và số lượng.")
    except Exception as e:
        print(f"Lỗi: {e}")

def sap_xep_theo_ten_hang():
    try:
        danh_sach_mat_hang.sort(key=lambda x: x["ten_hang"])
        print("Đã sắp xếp danh sách mặt hàng theo tên.")
    except Exception as e:
        print(f"Lỗi: {e}")

def menu():
    while True:
        print("\nQuản lý hàng hóa siêu thị")
        print("1. Xem danh sách mặt hàng")
        print("2. Nhập thông tin mặt hàng")
        print("3. Tính thành tiền và thuế VAT")
        print("4. Tìm và xóa mặt hàng theo mã")
        print("5. Tìm và chỉnh sửa mặt hàng theo mã")
        print("6. Xem danh sách mặt hàng sắp xếp theo tên")
        print("7. Thoát chương trình")

        try:
            lua_chon = int(input("Nhập lựa chọn của bạn: "))
            if lua_chon == 1:
                xem_danh_sach_mat_hang()
            elif lua_chon == 2:
                nhap_thong_tin_mat_hang()
            elif lua_chon == 3:
                tinh_thanh_tien_va_vat()
            elif lua_chon == 4:
                xoa_mat_hang_theo_ma()
            elif lua_chon == 5:
                chinh_sua_mat_hang_theo_ma()
            elif lua_chon == 6:
                sap_xep_theo_ten_hang()
            elif lua_chon == 7:
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số hợp lệ.")

# Chạy chương trình
menu()
