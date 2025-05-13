a = int(input("Nhập số thập phân: "))
b = oct(a)[2:]
print("Số bát phân là: ", b)
print(type(b))

'''
def bat_phan(a):
    while True:
        if a < 8:
            return str(a)
        else:
            b = ""
            while a != 0:
                b = str(a % 8) + b
                a = a // 8
            return b


print("Số thập phân %d trong hệ bát phân là %s " % (a, bat_phan(a)))
'''
