import math

# Nhập vào các cạnh của tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b <= c or a+c <= b or b+c<= a:
  print("Không phải là bộ ba cạnh của tam giác.")
else:
  if a == b and b == c:
    print("đây là bộ ba cạnh của tam giác đều.")
  # Kiểm tra tam giác cân có 2 TH
  elif a == b or b == c or a == c:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      print("Đây là tam giác vuông cân.")
    else :
      print("Đây là tam giác cân.")
  elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Đây là tam giác vuông.")
  else:
    print("Đây là tam giác thường.")
    