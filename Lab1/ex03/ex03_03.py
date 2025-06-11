def tao_tuple(lst):
    return tuple(lst)
input_list = input("Nhập các số, ngăn cách bởi giấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)