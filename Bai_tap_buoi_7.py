import string
import random
#bài 1
#a = string.ascii_lowercase
#b = string.ascii_uppercase
#c = string.digits
#d = string.punctuation
#tat_ca = a + b + c + d
#print(tat_ca)
#bài 2
#f = ["P", "Y", "T", "H", "O", "N"]
#e = "".join(f)
#print(e)
#Bài 3
#ask = int(input("Nhập độ dài mật khẩu:"))
#mk = "".join(random.choices(tat_ca, k=ask))
#print(mk)
#Bài 4
#ss = []
#for i in range(5):
    #s = random.randint(0, 9)
   # ss.append(s)
    
#print(ss)
#Bài 5
#a = string.ascii_lowercase
#b = string.ascii_uppercase
#c = string.digits
#d = string.punctuation
#all  = a + b + c + d
#do_dai = int(input("Nhập độ dài mật khẩu:"))
#if do_dai <4:
 #   print("Độ dài mật khẩu phải dài hơn để chứa đủ 4 nhóm ký tự")
#else:
   # mat_khau = [random.choice(a) + random.choice(b) + random.choice(c) + random.choice(d)]
   # mat_khau += random.choices(all, k=do_dai - 4)
   # random.shuffle(mat_khau)
   # ketqua = "".join(mat_khau)
    #  print("Kết quả mật khẩu:", ketqua)
#Bài 6
#do_dai = int(input("Nhập: "))

#if do_dai < 4:
  #  print("Kết quả:")
  #  print("Cần ít nhất 4 ký tự!")
#else:
    #print("Độ dài hợp lệ")
#Bài 7
#a = string.ascii_letters + string.digits + string.punctuation
#print("Kết quả(ví dụ):")
#for i in range(1,4):
    #b = "".join(random.choices(a, k=6))
    #print(f"Mật khẩu {i}: {b}")