
# tạo và nhập dữ liệu vào ma trận 
matrix_a = [
    [3,6,9],
    [6,6,6],
    [18,27,9]
]
n=3
for row in matrix_a:
    print(row)


#các phép tính với ma trận
#lưu ý các đoạn code về các phép toán không thể chạy chung trên 1 chương trình vì ma trận sau mỗi phép tính sẽ không còn là ma trận ban đầu
  #phép nhân
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n
for hang in matrix_a:
    print(hang)


  #phép chia
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] / n
for hang in matrix_a:
    print(hang)


  #phép cộng
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] + n
for hang in matrix_a:
    print(hang)
    
    
  #phép trừ
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] - n
for hang in matrix_a:
    print(hang)


 