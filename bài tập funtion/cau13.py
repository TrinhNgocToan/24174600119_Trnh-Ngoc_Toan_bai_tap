def phan_tich_thua_so_nguyen_to():
    n = int(input("Nhập một số nguyên dương: "))
    cac_thua_so = []
    i = 2
    while n > 1:  
        while n % i == 0:  
            cac_thua_so.append(i)
            n //= i
        i += 1  
    print("Thừa số nguyên tố của số đã nhập là:", " × ".join(map(str, cac_thua_so)))

phan_tich_thua_so_nguyen_to()
