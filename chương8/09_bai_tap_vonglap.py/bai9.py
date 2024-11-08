import math
n = int(input("Nhập n: "))
if n<=0:
    print("hãy nhập lại n")
else:
    print("Các số chính phương nhỏ hơn", n, "là:")
    for i in range(1, int(n**0.5) + 1):
        print(i*i, end=" ")
        