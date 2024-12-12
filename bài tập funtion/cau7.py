def tim_ucln():
    a = int(input("Nhập vào số thứ nhất: "))
    b = int(input("Nhập vào số thứ hai: ")) 
    if a > b:
        so_nhonhat = b  
    else:
        so_nhonhat = a  
    ucln = 1 
    for i in range(1, so_nhonhat + 1):
        if a % i == 0 and b % i == 0:
            ucln = i 
    print(f"Ước chung lớn nhất của {a} và {b} là {ucln}.")

tim_ucln()
