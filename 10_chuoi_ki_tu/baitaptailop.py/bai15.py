#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
ds_sinh_vien=[]
while True :
    print("MENU :")
    print("1. Xem danh sách sinh viên")
    print(" 2. Nhập thông tin sinh viên mới vào danh sách ")
    print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print("5. thoat chuong trinh")
    chon = input("Nhap so thu tu ban muoon lam")
    if chon.isdigit == False:
        print("Yêu vầu nhập lại ")
    else:
        chon = int(chon)
        if chon == 1:
            print("chạy 1")
            print(ds_sinh_vien)
        elif chon == 2:
            print("chạy 2")
            sinh_vien = {"ma_sinh_vien":"",
                         "ho_dem":"",
                         "ten":"",
                         "diem_toan":0.0,
                         "diem_li":0.0,
                         "diem_hoa":0.0,
                         "diem_tb":0.0,
                         }
            #cách 1 yêu cầu nhập vào số lượng sv cần nhập
            n=input(print("nhap vao so sinh vien can nhap"))
            # thêm kiểm tra 
            n = int(n)
            for sv in range (n):
                print("sinh vien thu{sv+1}")
                sinh_vien = "ma_sinh_vien":"",
                "ho_dem":"",
                "ten":"",
                
        elif chon == 3:
            print("chạy 3")
        elif chon == 4:
            print("chạy 4")
        elif chon == 5:
            print("thoát chương trình")
            break
        else:
            print("yêu cầu nhập lại")
        
        
