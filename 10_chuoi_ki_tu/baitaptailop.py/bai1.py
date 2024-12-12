ds_so = []

while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if not n.isdigit():  
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break
for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        if so.lstrip('-').replace('.', '', 1).isdigit():  
            so = float(so)  
            ds_so.append(so)  
            break 
        else:
            print("Bạn hãy nhập lại!")
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")
