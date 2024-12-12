def la_so_nguyen_to(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True  


def gia_tri_trung_binh_so_nguyen_to():
    day_so = input("Nhập một dãy số nguyên, cách nhau bởi dấu phẩy: ")
    cac_so = list(map(int, day_so.split(',')))
    so_nguyen_to = [so for so in cac_so if la_so_nguyen_to(so)]
    if len(so_nguyen_to) != len(cac_so):
        print("Dãy nhập vào có chứa số không phải số nguyên tố.")
    else:
        tong = sum(so_nguyen_to)
        trung_binh = tong / len(so_nguyen_to)
        print(f"Giá trị trung bình của dãy số nguyên tố là: {trung_binh:.2f}")


gia_tri_trung_binh_so_nguyen_to()
