tailieu = input("Nhập tên file: ")


def doc_file(tailieu):
    try:
        with open(tailieu, "r", encoding="utf-8") as f:
            data = f.readlines()
        return data
    except FileNotFoundError:
        print(f"File {tailieu} không tồn tại.")
        return None


doc_file(tailieu)
