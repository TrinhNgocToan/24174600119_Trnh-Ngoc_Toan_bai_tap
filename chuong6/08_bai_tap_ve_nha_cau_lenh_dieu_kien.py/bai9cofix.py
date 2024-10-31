xe = int(input("Bạn muốn thuê xe 4 chỗ hay 7 chỗ? (Nhập 4 hoặc 7): "))
so_km = float(input("Nhập số km bạn muốn đi: "))
tg_cho = float(input("Nhập thời gian chờ (phút): "))
tienxe = 0
if xe == 4 or xe == 7 and so_km > 0 and tg_cho >= 0:
    # Tính phí xe 4 chỗ
    if xe == 4:
        tienxe += 11_000 / 0.8  # Giá mở cửa
        if so_km > 0.8:
            if so_km <= 20:
                tienxe += (so_km - 0.8) * 12_100
            else:
                tienxe += (20 - 0.8) * 12_100 + (so_km - 20) * 10_000
    # Tính cước phí cho xe 7 chỗ
    else:
        tienxe += 13_000 / 0.8  # Giá mở cửa
        if so_km > 0.8:
            if so_km <= 30:
                tienxe += (so_km - 0.8) * 14_100
            else:
                tienxe += (30 - 0.8) * 14_100 + (so_km - 30) * 12_000
    # Tính tiền chờ
    if tg_cho > 5:
        phi_cho = (tg_cho - 5) * 800
    else:
        phi_cho = 0
    # Tổng cước phí
    tong_cuoc_phi = tienxe + phi_cho
    print(f"Tổng cước phí là: {tong_cuoc_phi:.0f} đồng")        
else:
    print("Hãy nhập lại, chỉ có thể thuê xe 4 chỗ hoặc 7 chỗ. số km phải lớn hơn 0. tg chờ không được âm")