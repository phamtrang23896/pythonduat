# Tính tổng hai số nguyên có xử lý ngoại lệ
def sum_two_numbers():
    try:
        num1 = int(input("Nhập số nguyên thứ nhất: "))
        num2 = int(input("Nhập số nguyên thứ hai: "))
        total = num1 + num2
        print(f"Tổng hai số là: {total}")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")


# Chạy hàm
sum_two_numbers()
