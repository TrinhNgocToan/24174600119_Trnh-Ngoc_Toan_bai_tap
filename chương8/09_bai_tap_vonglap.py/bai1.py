#Sử dụng vòng lặp for in ra màn hình các số nguyên dương lẻ nhỏ hơn 100
n = int(input("Nhập n nguyên dương là :"))
if n > 0 :
    for i in range(n + 1):
        if i  % 2 != 0 :
            print(f"dãy các số nguyên dương là {i} :")
else :
    print("Bạn đã nhập sai n , hãy nhập lại ")