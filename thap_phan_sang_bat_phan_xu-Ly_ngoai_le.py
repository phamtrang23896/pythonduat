def new_func():
    try:
        stp = int(input("Nhập số thập phân: "))
        a = oct(stp)[2:]
        print(f"So thap phan {stp} trong he bat phan la {a}")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


new_func()
