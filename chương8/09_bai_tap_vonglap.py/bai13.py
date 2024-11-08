import math
# Nhập số nguyên dương
n = int(input("Nhập một số nguyên dương: "))
# Phân tích thừa số nguyên tố
i = 2
print("Phân tích thừa số nguyên tố của", n, "là:")
while i * i <= n:
  while n % i == 0:
    print(i, end=" ")
    n //= i
  i += 1
if n > 1:
  print(n)