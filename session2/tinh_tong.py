st = int(input("nhap vao gia tri khoi dau"))
en = int(input("nhap vao gia tri ket thuc"))
r = range(st, en + 1)
a = 0
for i in r:
    a = a + i
print("ket qua tinh tong la:",a)