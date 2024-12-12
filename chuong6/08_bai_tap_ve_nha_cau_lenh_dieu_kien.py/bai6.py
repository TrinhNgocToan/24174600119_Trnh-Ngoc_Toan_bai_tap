print("----- Rạp Chiếu Phim -----")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
# Nhập lựa chọn từ người dùng
chon = input("Nhập số tương ứng với thể loại phim bạn muốn xem: ")
# Xử lý lựa chọn
if chon == '1':
    print("Bạn đã chọn Phim tình cảm.")
elif chon == '2':
    print("Bạn đã chọn Phim kinh dị.")
elif chon == '3':
    print("Bạn đã chọn Phim hoạt hình.")
elif chon == '4':
    print("Bạn đã chọn Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")