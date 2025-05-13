def tinh_tong():
    day = input("Nhập dãy số cách nhau bởi dấu cách: ")
    day = day.split()
    tong = 0
    for i in range(len(day)):
        tong = tong + int(day[i])
    print("Tổng các số trong dãy là:", tong)


tinh_tong()

"""
num_series = map(int,input("Nhập dãy các số nguyên vào: ").split())

print(f"Tổng của dãy số: {sum(num_series)}")

"""
