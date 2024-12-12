def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1, n):  
        if n % i == 0:     
            tong_uoc += i  
    return tong_uoc == n   

def so_hoan_hao_nho_nhat():
    day_so = input("Nhập một dãy số nguyên, cách nhau bởi dấu phẩy: ")
    cac_so = list(map(int, day_so.split(',')))
    cac_so_hoan_hao = [so for so in cac_so if la_so_hoan_hao(so)]
    if cac_so_hoan_hao:
        so_nho_nhat = min(cac_so_hoan_hao)
        print(f"Số hoàn hảo nhỏ nhất trong dãy là: {so_nho_nhat}")
    else:
        print("Không có số hoàn hảo nào trong dãy.")

so_hoan_hao_nho_nhat()
