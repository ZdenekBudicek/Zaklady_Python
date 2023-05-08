def change(x_list):
    result_list = []
    for item in x_list:
        item = item + 10
        result_list.append(item)
    print(result_list)


change([1, 2, 3, 4, 5])
