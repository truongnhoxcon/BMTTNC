def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Nhập chuỗi cần đảo ngược: ")
print("Chuỗi đã đảo ngược là: ", dao_nguoc_chuoi(input_str))