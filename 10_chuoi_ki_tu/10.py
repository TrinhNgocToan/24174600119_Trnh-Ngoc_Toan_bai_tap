# # Bài 10: Viết chương trình nhập vào một chuỗi ký tự, trả về kết quả chuỗi mới sau khi dồn tất cả số sang bên trái
# Ví dụ: Nhập vào: “Xsn61ssakdu271626s  1231  12”
#              Trả về: “61271626123112Xsnssakdus   ”
chuoi = input("Nhập vào chuỗi ký tự: ")
so  = ''
chu = ''
for i in chuoi:
    if i.isdigit():
        so += i
    else:
        chu += i
print("Kết quả:", so + chu)