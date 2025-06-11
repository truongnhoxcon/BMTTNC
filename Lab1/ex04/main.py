from QuanLySinhVien import QuanLySinhVien

QuanLySinhVien = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("***************MENU***************")
    print("** 1. Them sinh vien.           **")
    print("** 2. Cap nhat thong tin sinh vien boi ID. **")
    print("** 3. Xoa sinh vien boi ID.     **")
    print("** 4. Tim kiem sinh vien theo ten. **")
    print("** 5. Sap xep sinh vien theo diem trung binh. **")
    print("** 6. Sap xep sinh vien theo ten chuyen nganh. **")
    print("** 7. Hien thi danh sach sinh vien. **")
    print("** 0. Thoat                     **")
    print("*********************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        QuanLySinhVien.nhapSV()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (QuanLySinhVien.soLuongSV() > 0):
            print("\n2. Cap nhat thong tin sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            QuanLySinhVien.updateSV(ID)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 3):
        if (QuanLySinhVien.soLuongSV() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (QuanLySinhVien.deleteByIDD(ID)):
                print("\nSinh vien co id = ", ID, " da bi xoa.")
            else:
                print("\nSinh vien co id = ", ID, " khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 4):
        if (QuanLySinhVien.soLuongSV() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = QuanLySinhVien.findByName(name)
            QuanLySinhVien.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 5):
        if (QuanLySinhVien.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            QuanLySinhVien.sortByDiemTB()
            QuanLySinhVien.showSinhVien(QuanLySinhVien.getListSV())
        else:
            print("\nDanh sach sinh vien trong!")
        
    elif (key == 6):
        if (QuanLySinhVien.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
            QuanLySinhVien.sortByTenChuyenNganh()
            QuanLySinhVien.showSinhVien(QuanLySinhVien.getListSV())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 7):
        if (QuanLySinhVien.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            QuanLySinhVien.showSinhVien(QuanLySinhVien.getListSV())
        else:
            print("\nDanh sach sinh vien trong!")

    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
