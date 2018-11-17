
def add_matrices(a, b):
    if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
        raise ValueError("Różny kształt")

    result = []
    for row_i in range(len(a)):
        # print(f"Wiersze: {row_i} z obu macierzy:")
        # print('a:', a[row_i])
        # print('b:', b[row_i])
        new_row = []
        for col_i in range(len(a[row_i])):
            new_row.append(a[row_i][col_i] + b[row_i][col_i])
        result.append(new_row)
    return result



def sub_matrices(a,b):
    if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
        raise ValueError("Różny kształt")

    result = []
    for row_i in range(len(a)):
        # print(f"Wiersze: {row_i} z obu macierzy:")
        # print('a:', a[row_i])
        # print('b:', b[row_i])
        new_row = []
        for col_i in range(len(a[row_i])):
            new_row.append(a[row_i][col_i] + b[row_i][col_i])
        result.append(new_row)
    return result

a = [
    [1, 2, 3],
    [4, 5, 6],
]

b = [
    [7, 8, 9],
    [10, 11, 12],
]

result = add_matrices(a,b)
print(result)