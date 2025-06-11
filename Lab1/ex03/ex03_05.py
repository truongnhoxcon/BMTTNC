def count(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_str = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_str.split()
so_lan_xuat_hien = count(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)