so_gio_lam = float(input("Nhập số giờ làm của nhân viên: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ theo tiêu chuẩn: "))
gio_tieuchuan = 44
gio_vuot_tieuchuan = max(0, so_gio_lam - gio_tieuchuan)
thuc_linh = gio_tieuchuan * luong_gio + gio_vuot_tieuchuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")