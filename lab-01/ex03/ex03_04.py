def truy_cap_phan_tu(typle_data):
    first_element = typle_data[0]
    last_element = typle_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập vào một tuple, ví dụ (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên: ", first)
print("Phần tử cuối cùng: ", last)