#import random, string
#do_dai = int(input("Nhập độ dài mật khẩu(phải ít nhất 4 ký tự): "))
#a = string.ascii_lowercase
#b = string.ascii_uppercase
#c = string.digits
#d = string.punctuation
#tat_ca = a + b + c + d
#if do_dai < 4:
 #   print("Độ dài mật khẩu phải dài hơn để chứa đủ 4 nhóm ký tự")
#else:
   # mat_khau = [random.choice(a), random.choice(b), random.choice(c), random.choice(d)]
    #mat_khau += random.choices(tat_ca, k=do_dai - 4)
    #mk = "".join(mat_khau)
    #random.shuffle(list(mk))
    #print("Kết quả mật khẩu:", mk)