text = lambda x: x * 7

print(text(7))


# Use of lambda() with filter()

arr_lst = [2, 3, 4, 4, 54, 22, 36]

lambda_lst = list(filter(lambda x: (x % 2 != 0), arr_lst))
print(lambda_lst)

# Use of lambda() with map()
map_lst = list(map(lambda x: x * 2, arr_lst))
print(map_lst)

