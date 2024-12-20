m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
ma_tran = []

print("Nhập các phần tử cho ma trận:")
for i in range(m):
    hang = []  
    for j in range(n):
        so = int(input(f"Nhập phần tử tại hàng {i + 1}, cột {j + 1}: "))
        hang.append(so) 
    ma_tran.append(hang) 

print("\nMa trận đã nhập là:")
for hang in ma_tran:
    print(" ".join(map(str, hang)))  
