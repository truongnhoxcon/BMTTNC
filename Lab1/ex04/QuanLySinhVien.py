from SinhVien import SinhVien

class QuanLySinhVien:
    listSV = []
    def generateID(self):
        maxID = 1
        if(self.soLuongSV() > 0):
            maxID = self.listSV[0]._id
            for sv in self.listSV:
                if(maxID < sv._id):
                    maxID = sv._id
            maxID += 1  
        return maxID
    
    def soLuongSV(self):
        return len(self.listSV)

    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhập họ tên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập chuyên ngành: ")
        diemTB = float(input("Nhập điểm TB: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLLoaiHocLuc(sv)
        self.listSV.append(sv)

    def updateSV(self):
        sv:SinhVien = self.findByIDfindByID()
        if(sv != None):
            name = input("Nhập họ tên: ")
            sex = input("Nhập giới tính: ")
            major = int(input("Nhập chuyên ngành: "))
            diemTB = float(input("Nhập điểm TB: "))
            sv._name = name
            sv._sex = sex
            sv._major = major   
            sv._diemTB = diemTB
            self.xepLLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có ID = {}".format(id))
    def sortByID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)
    def sortByName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)
    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        id = int(input("Nhập mã sinh viên: "))
        if self.soLuongSV() > 0:
            for sv in self.listSV:
                if sv._id == ID:
                    searchResult = sv
                    break
        return searchResult
    def deleteByID(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSV.remove(sv)
            isDelete = True
        return isDelete 
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8.0):
            sv._hocLuc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >= 5.0):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
            
    def showSinhVien(self, listSV):
        print ("{:<8}, {:<18}, {:<8}, {:<8}, {:<8}, {:<8}".format("ID", "Họ tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        if(listSV._len_() > 0):
            for sv in listSV:
                print ("{:<8}, {:<18}, {:<8}, {:<8}, {:<8}, {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSV(self):
        return self.listSV