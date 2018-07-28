ls = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

def sum_lists(ls):
    len1 = len(ls)
    len2 = len(ls[0])

    for i in range(1, len1):
        for j in range(len2):
            ls[0][j] = ls[0][j] + ls[i][j]

    return ls[0]