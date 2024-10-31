#Bài 1
y = float(input("Nhập số năm: "))
if y >= 0:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print ("Là năm nhuận ")
    else:
        print("Không là năm nhuận")
else:
    print("Không tồn tại bài toán")
print("Kết thúc chương trình")