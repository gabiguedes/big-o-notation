def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Valor não encontrado na lista')

data = [1, 3, 7, 5, 9, 0, 11]
print(linear_search(data, 9))