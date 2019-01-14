import numpy as np



def getMatrix2DConverter(diffDict, x_list, y_list):
    mat = np.ndarray(shape=(len(x_list),len(y_list)))
    for i,k1 in enumerate(x_list):
        for j,k2 in enumerate(y_list):
            mat[i][j] = diffDict[k1][k2]
    return mat

def normalize(matrix, path='./model/tmpResult.npy', row_col_name_list=None):
    import copy
    mat = copy.deepcopy(matrix)
    for idx, _mat in enumerate(mat):
        sum = np.sum(_mat)
        if sum == 0:
            continue
        matrix[idx] = (_mat/sum)#.round(6)
    np.save(path, matrix)


if __name__ == "__main__":
    import TypoDataAnalyzer.CONST as const
    import csv

    x_label_list = const.char_list
    y_label_list = const.char_list

    res = dict()

    with open('randomTrain.csv', 'r') as fp:
        cr = csv.reader(fp)
        for row, x in zip(cr, x_label_list):
            if x not in res:
                res[x] = dict()
            for val, y in zip(row, y_label_list):
                res[x][y] = int(val)
    normalize(getMatrix2DConverter(res, x_label_list, y_label_list))


