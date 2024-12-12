def ktrasothuc():
    n = input("Nhập vào n: ")
    if n.count('.') <= 1 and n.replace('.', '', 1).replace('-', '', 1).isdigit():
        if n.startswith('-') and len(n) == 1:
            print("Đây không phải là số thực.")
        else:
            print("Đây là số thực.")
    else:
        print("Đây không phải là số thực.")

ktrasothuc()