import random
import string

tiep_tuc = "y"

while tiep_tuc.lower() == "y":
    # Nhập thông tin
    phuong_tien = input(
        "Nhập phương tiện đi lại (xe máy, ô tô, xe buýt, tàu hỏa, máy bay): "
    )

    quang_duong = float(input("Nhập quãng đường (km): "))
    muc_tieu_thu = float(input("Nhập mức tiêu thụ nhiên liệu (lít/100km): "))
    so_nguoi = int(input("Nhập số người: "))

    # Kiểm tra dữ liệu
    if quang_duong <= 0:
        print("Quãng đường không hợp lệ")
        continue

    if muc_tieu_thu <= 0:
        print("Mức tiêu thụ nhiên liệu không hợp lệ")
        continue

    if so_nguoi <= 0:
        print("Số người không hợp lệ")
        continue

    if phuong_tien.lower() not in ["xe máy", "ô tô", "xe buýt", "tàu hỏa", "máy bay"]:
        print("Phương tiện không hợp lệ")
        continue

    # Tạo mã chuyến đi
    ma_chuyen_di = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=6)
    )

    # XE MÁY
    if phuong_tien.lower() == "xe máy":

        loai_xang = input("Nhập loại xăng (A95, A92, E5): ")

        if loai_xang.upper() == "A95":
            gia_xang = 25000
        elif loai_xang.upper() == "A92":
            gia_xang = 23000
        elif loai_xang.upper() == "E5":
            gia_xang = 22000
        else:
            print("Loại xăng không hợp lệ")
            continue

        tong_chi_phi = quang_duong * muc_tieu_thu / 100 * gia_xang
        chi_phi_moi_nguoi = tong_chi_phi / so_nguoi

        print("\n-THÔNG TIN CHUYẾN ĐI-")
        print("Phương tiện:", phuong_tien)
        print("Quãng đường:", quang_duong, "km")
        print("Mức tiêu thụ:", muc_tieu_thu, "lít/100km")
        print("Loại xăng:", loai_xang.upper())
        print("Số người:", so_nguoi)
        print(f"Tổng chi phí chuyến đi bằng {phuong_tien} là: {round(tong_chi_phi):,} VND")
        print(f"Chi phí mỗi người: {round(chi_phi_moi_nguoi):,} VND")
        print(f"Mã chuyến đi: {ma_chuyen_di}")

    # Ô TÔ
    elif phuong_tien.lower() == "ô tô":

        loai_xang = input("Nhập loại xăng (A95, A92, E5): ")

        if loai_xang.upper() == "A95":
            gia_xang = 25000
        elif loai_xang.upper() == "A92":
            gia_xang = 23000
        elif loai_xang.upper() == "E5":
            gia_xang = 22000
        else:
            print("Loại xăng không hợp lệ")
            continue

        tong_chi_phi = quang_duong * muc_tieu_thu / 100 * gia_xang
        chi_phi_moi_nguoi = tong_chi_phi / so_nguoi

        print("\n-THÔNG TIN CHUYẾN ĐI-")
        print("Phương tiện:", phuong_tien)
        print("Quãng đường:", quang_duong, "km")
        print("Mức tiêu thụ:", muc_tieu_thu, "lít/100km")
        print("Loại xăng:", loai_xang.upper())
        print("Số người:", so_nguoi)
        print(f"Tổng chi phí chuyến đi bằng {phuong_tien} là: {round(tong_chi_phi):,} VND")
        print(f"Chi phí mỗi người: {round(chi_phi_moi_nguoi):,} VND")
        print(f"Mã chuyến đi: {ma_chuyen_di}")

    # XE BUÝT
    elif phuong_tien.lower() == "xe buýt":
        loai_xang = input("Nhập loại xăng (A95, A92, E5): ")
        if loai_xang.upper() == "A95":
            gia_xang = 25000
        elif loai_xang.upper() == "A92":
            gia_xang = 23000
        elif loai_xang.upper() == "E5":
            gia_xang = 22000
        else:
            print("Loại xăng không hợp lệ")
            continue

        chi_phi_nhien_lieu = quang_duong * muc_tieu_thu / 100 * gia_xang
        chi_phi_ve = quang_duong * 5000 * so_nguoi
        tong_chi_phi = chi_phi_nhien_lieu + chi_phi_ve

        print("\n-THÔNG TIN CHUYẾN ĐI-")
        print("Phương tiện:", phuong_tien)
        print("Quãng đường:", quang_duong, "km")
        print("Mức tiêu thụ:", muc_tieu_thu, "lít/100km")
        print("Loại xăng:", loai_xang.upper())
        print("Số người:", so_nguoi)
        print("Chi phí nhiên liệu:", round(chi_phi_nhien_lieu), "VND")
        print("Chi phí vé:", round(chi_phi_ve), "VND")
        print(f"Tổng chi phí chuyến đi bằng {phuong_tien} là: {round(tong_chi_phi):,} VND")
        print(f"Mã chuyến đi: {ma_chuyen_di}")

    # TÀU HỎA
    elif phuong_tien.lower() == "tàu hỏa":
        chi_phi_ve = quang_duong * 10000
        tong_chi_phi = chi_phi_ve * so_nguoi

        print("\n-THÔNG TIN CHUYẾN ĐI-")
        print("Phương tiện:", phuong_tien)
        print("Quãng đường:", quang_duong, "km")
        print("Số người:", so_nguoi)
        print(f"Chi phí chuyến đi bằng {phuong_tien} là: {round(tong_chi_phi):,} VND")
        print(f"Mã chuyến đi: {ma_chuyen_di}")

    # MÁY BAY
    elif phuong_tien.lower() == "máy bay":
        chi_phi_ve = quang_duong * 3000
        tong_chi_phi = chi_phi_ve * so_nguoi

        print("\n-THÔNG TIN CHUYẾN ĐI-")
        print("Phương tiện:", phuong_tien)
        print("Quãng đường:", quang_duong, "km")
        print("Số người:", so_nguoi)
        print(f"Chi phí chuyến đi bằng {phuong_tien} là: {round(tong_chi_phi):,} VND")
        print(f"Mã chuyến đi: {ma_chuyen_di}")

    tiep_tuc = input("\nBạn có muốn tính chi phí chuyến đi tiếp theo không? (y/n): ")

print("Cảm ơn bạn đã sử dụng chương trình!")