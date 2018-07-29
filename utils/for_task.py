ls = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def sum_lists(ls):
    len1 = len(ls)
    len2 = len(ls[0])
    rs = [0 for i in range(len2)]

    for i in range(0, len1):
        for j in range(len2):
            rs[j] = ls[0][j] + ls[i][j]

    return rs


print(sum_lists(ls))
