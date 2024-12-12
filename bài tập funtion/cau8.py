def tim_uoc():
    ds_uoc=[]
    n = int(input("Nhập vào một số nguyên: "))
    print(f"Các ước của {n} là:")
    for i in range(1, n + 1):
        if n % i == 0:  
             ds_uoc.append(i)
    print(ds_uoc)


tim_uoc()
