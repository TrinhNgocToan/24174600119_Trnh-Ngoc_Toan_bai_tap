# Khởi tạo ma trận A
A = [
    [1, 2, 3],
    [4, 5, 6]
]
# tạo ma trận chuyển vị với kích thước ngược lại
A_T = [[0] * len(A) for _ in range(len(A[0]))]
# chuyển vị
for i in range(len(A)):
    for j in range(len(A[0])):
        A_T[j][i] = A[i][j]
print("Ma trận chuyển vị A^T:")
for row in A_T:
    print(row)
