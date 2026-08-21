#TÍNH CHI PHÍ CHUYẾN ĐI
import random, string
phuong_tien = input("Nhập phương tiện đi lại (xe máy, ô tô, xe buýt, tàu hỏa, máy bay): ")
quang_duong = float(input("Nhập quãng đường(km): "))
loai_xang = input("Nhập loại xăng (A95, A92, E5): ")
muc_tieu_thu = float(input("Nhập mức tiêu thụ nhiên liệu (lít/100km): "))
if phuong_tien.lower() == "xe máy":
    if loai_xang.upper() == "A95":
        gia_xang = 25000
    elif loai_xang.upper() == "A92": #Loại xăng
        gia_xang = 23000
    elif loai_xang.upper() == "E5":
        gia_xang = 22000
    else:
        print("Loại xăng không hợp lệ")
        exit()
    chi_phi = quang_duong * muc_tieu_thu / 100 * gia_xang #Tính chi phí chuyến đi theo VND
    print(f"Chi phí chuyến đi bằng {phuong_tien} là: {chi_phi} VND")
    ma_chuyen_di = "".join(random.choices(string.ascii_uppercase + string.digits, k=6)) #TẠO MÃ CHUYẾN ĐI
    print(f"Mã chuyến đi: {ma_chuyen_di}")
elif phuong_tien.lower() == "ô tô":
    if loai_xang.upper() == "A95":
        gia_xang = 25000
    elif loai_xang.upper() == "A92": #Loại xăng
        gia_xang = 23000
    elif loai_xang.upper() == "E5":
        gia_xang = 22000
    else:
        print("Loại xăng không hợp lệ")
        exit()
    chi_phi = quang_duong * muc_tieu_thu / 100 * gia_xang #Tính chi phí chuyến đi theo VND
    print(f"Chi phí chuyến đi bằng {phuong_tien} là: {chi_phi} VND")
    ma_chuyen_di = "".join(random.choices(string.ascii_uppercase + string.digits, k=6)) #TẠO MÃ CHUYẾN ĐI
    print(f"Mã chuyến đi: {ma_chuyen_di}")
    
    
    
