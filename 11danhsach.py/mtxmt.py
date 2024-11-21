# Ma trận A và B
A = [
    [1, 2],
    [4, 5],
    [7, 8]
]
B = [
    [9, 8,9],
    [6, 5,6]
]
# Kiểm tra điều kiện nhân ma trận (số cột của A phải bằng số hàng của B)
if len(A[0]) != len(B):
    print("Không thể nhân ma trận, số cột của A phải bằng số hàng của B.")
else:
    #sau khi nhân sẽ cho ra ma trận mới C có kích cỡ số hàng của A và số cột của B
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    # Nhân ma trận A với ma trận B
    for i in range(len(A)):  # Duyệt qua từng hàng của ma trận A
        for j in range(len(B[0])):  # Duyệt qua từng cột của ma trận B
            for k in range(len(B)):  # Duyệt qua từng phần tử trong hàng A và cột B
                C[i][j] =C[i][j]+ (A[i][k] * B[k][j])
    print("Ma trận kết quả (C = A * B):")
    for row in C:
        print(row)
