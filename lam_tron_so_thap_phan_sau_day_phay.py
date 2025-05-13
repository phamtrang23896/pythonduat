# in ra biểu thị cần điền
print("nhập giá trị cần lầm tròn")
# ép kiểu và điền giá trị
a = float(input())
# in ra và điền giá trị tiếp theo
print("số chữ số xuất hiện trong giá trị vừa nhập")
b = int(input())
print("{0:.{1}f}".format(a, b))
""" dùng round
c = round(a, b)  # làm tròn số a với b chữ số
print("Số sau khi làm tròn ", c)
"""

"""
#xử lí bài toán
from decimal import*
getcontext().prec = b
print(Decimal(a)/Decimal(1))
"""
