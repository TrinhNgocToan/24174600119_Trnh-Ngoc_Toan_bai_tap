# kiểm tra nhập vào n
while True:
    n = input("Nhập vào số nguyên dương n: ")
    if n.isdigit() == False:
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break

#tìm các số lẻ,chăne bé hơn n
A=[]
B=[]
for i in range (1,n,1):
    if i % 2 != 0 and i < n:
        A.append(i)
    if i % 2 == 0 and i < n:
        B.append(i)
# In kết quả
print("cac so le nho hon n ",A)
print("cac so le nho hon n ",B)
