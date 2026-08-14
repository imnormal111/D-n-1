import random, string
#Bài 1
#a = string.ascii_lowercase
#b = string.ascii_uppercase
#c = string.digits
#d = string.punctuation
#tat_ca = a + b + c + d
#print(tat_ca)
#Bài 2
#a = ["P", "Y", "T", "H", "O", "N"]
#a = "".join(a)
#print(a)
#Bài 3
#tat_ca = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#ask = int(input("Nhập độ dài mật khẩu:"))
#mk = "".join(random.choices(tat_ca, k=ask))
#print(mk)
#Bài 4
# s=[]
# for i in range(5):
#     s = random.randint(0, 9)
#     s.append(s)
#print(s)
#Bài 5&6
#a = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#do_dai = int(input("Nhập độ dài mật khẩu:"))
#if do_dai < 4:
  #  print("Độ dài mật khẩu phải dài hơn để chứa đủ 4 nhóm ký tự")  
#else:
    #mat_khau = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.punctuation)]
   # mat_khau += random.choices(a, k=do_dai - 4)
   # random.shuffle(mat_khau)
    #ketqua = "".join(mat_khau)
    #print("Kết quả mật khẩu:", ketqua)
#Bài 7
#a = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
#print("Kết quả(ví dụ):")
#for i in range(1,4):
   # b = "".join(random.choices(a, k=10))
   # print(f"Mật khẩu {i}: {b}")