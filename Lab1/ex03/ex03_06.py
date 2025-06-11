def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else: 
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd' : 4}
keydel = 'b'
result = xoa_phan_tu(my_dict, keydel)
if result: 
    print("Phần tử đã xoá từ dictionary: ", my_dict)
else:
    print("Không tìm thấy phần tử trong dictionary.")