import random, string
do_dai = int(input("Nhập độ dài mật khẩu(phải ít nhất 4 ký tự): "))
a = string.ascii_lowercase #
b = string.ascii_uppercase 
c = string.digits 
d = string.punctuation 
tat_ca = a + b + c + d #tổng kho kí tự(chữ thường, hoa, số, ký tự đặc biệt)
if do_dai < 4: #Kiểm tra xem độ dài trên 4(để đủ 4 nhóm ký tự)
    print("Độ dài mật khẩu phải dài hơn để chứa đủ 4 nhóm ký tự")
else:
    mat_khau = [random.choice(a), random.choice(b), random.choice(c), random.choice(d)]
    mat_khau += random.choices(tat_ca, k=do_dai - 4)
    mk = "".join(mat_khau) #Join để nối các ký tự thành chuỗi
    random.shuffle(list(mk))
if do_dai < 8:
    print("Mật khẩu yếu")
elif do_dai <= 11:
    print("Mật khẩu trung bình")
else:
    print("Mật khẩu mạnh")
print("Mật khẩu:", mk)