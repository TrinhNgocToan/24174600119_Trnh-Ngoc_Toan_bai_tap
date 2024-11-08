n=int(input("nhập vào n"))
if n <= 1:
    print("n không hợp lệ nhập lại n")
else:
    k=n
    for i in range (n+1):
        if k%n==0 and k!=n and k!=1:
            print(f"ko phải là số nguyên tố")
            break
        k=k-1
    else:
        print("đây là số nguyên tố")