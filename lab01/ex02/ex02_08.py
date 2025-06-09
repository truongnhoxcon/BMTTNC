def chia_het_cho_5(so_nhi_phan):
    try:
        so_thap_phan = int(so_nhi_phan, 2)
        return so_thap_phan % 5 == 0
    except:
        return False

chuoi_nhap = input("Nhập chuỗi các số nhị phân (phân tách bởi dấu phẩy): ")
ds_so = chuoi_nhap.split(',')

ket_qua = []
for so in ds_so:
    if chia_het_cho_5(so.strip()):
        ket_qua.append(so.strip())

print("Các số nhị phân chia hết cho 5 trong chuỗi đã cho là:")
print(",".join(ket_qua))
