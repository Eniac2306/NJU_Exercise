def lcs_mat(list1, list2):
    m = len(list1)
    n = len(list2)
    mat = [[0] * (n + 1) for row in range(m + 1)]
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if list1[row - 1] == list2[col - 1]:
                mat[row][col] = mat[row - 1][col - 1] + 1
            else:
                mat[row][col] = max(mat[row][col - 1], mat[row - 1][col])
    return mat


def all_lcs(lcs_dict, mat, list1, list2, index1, index2):
    if ((index1, index2) in lcs_dict): return lcs_dict[(index1, index2)]
    if (index1 == 0) or (index2 == 0):
        return [[]]
    elif list1[index1 - 1] == list2[index2 - 1]:
        lcs_dict[(index1, index2)] = [prevs + [list1[index1 - 1]] for prevs in
                                      all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2 - 1)]
        return lcs_dict[(index1, index2)]
    else:
        lcs_list = []
        if mat[index1][index2 - 1] >= mat[index1 - 1][index2]:
            before = all_lcs(lcs_dict, mat, list1, list2, index1, index2 - 1)
            for series in before:
                if not series in lcs_list: lcs_list.append(series)
        if mat[index1 - 1][index2] >= mat[index1][index2 - 1]:
            before = all_lcs(lcs_dict, mat, list1, list2, index1 - 1, index2)
            for series in before:
                if not series in lcs_list: lcs_list.append(series)
        lcs_dict[(index1, index2)] = lcs_list
        return lcs_list


def lcs(list1, list2):
    mapping = dict()
    return all_lcs(mapping, lcs_mat(list1, list2), list1, list2, len(list1), len(list2));


s1 = list(input())
s2 = list(input())
for s in lcs(s1, s2):
    print("".join(s))
