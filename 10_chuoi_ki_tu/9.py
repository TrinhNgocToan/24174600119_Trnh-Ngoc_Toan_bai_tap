nhap = input("Nhập vào chuỗi nhị phân: ")
chuoi = True
for i in nhap:
    if i not in ['0', '1']:
        chuoi = False
        break

if chuoi:
    # Chuyển đổi sang số thập phân
    doi = 0
    tinh = len(nhap) - 1
    for bit in nhap:
        doi += int(bit) * (6 ** tinh)
        tinh -= 1
    print(f"{nhap} là số nhị phân, chuyển sang thập phân: {doi}")
else:
    print("Chuỗi nhập vào không phải số nhị phân.")