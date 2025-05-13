day_Gia_Tri = input("Nhập dãy số cách nhau bởi dấu cách: ")
danh_Sach_Gia_Tri = day_Gia_Tri.split()
try:
    danh_Sach_So = map(int, danh_Sach_Gia_Tri)

    tong_Day_So = sum(danh_Sach_So)

    print(tong_Day_So)
except ValueError:
    print("dinh dang dau vao khong hop le!")
