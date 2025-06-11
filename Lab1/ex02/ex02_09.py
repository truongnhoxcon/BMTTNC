def kiem_tra_so_ngto(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhập vào một số nguyên: "))
if kiem_tra_so_ngto(number):
    print(number, "Là số nguyễn tố.")
else: 
    print(number, "Không phải là số nguyên tố.")