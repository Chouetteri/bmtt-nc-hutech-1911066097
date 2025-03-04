def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập vào một list các số nguyên cách nhau bởi dấu phẩy: ")
number = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(number)
print(f"List sau khi đảo ngược là: {list_dao_nguoc}")