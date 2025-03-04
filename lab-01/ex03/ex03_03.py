def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập vào một danh sách các số, cách nhau bởi dấu phẩy: ")
number = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(number)
print("List: ", number)
print("Tuple từ List: ", my_tuple)