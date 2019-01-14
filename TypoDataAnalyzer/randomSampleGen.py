
import TypoDataAnalyzer.CONST as const
import random
def generate():
    x_label_list = const.char_list
    y_label_list = const.char_list

    res = dict()
    for x in x_label_list:
        if x not in res:
            res[x] = dict()
        for y in y_label_list:
            if x == y:
                res[x][y] = 0
            res[x][y] = random.randrange(1,100)
    import csv
    with open('randomTrain.csv', 'w') as fp:
        c = csv.writer(fp)
        for x in x_label_list:
            row = list(res[x].values())
            c.writerow(row)
            #for y in y_label_list:


if __name__ == "__main__":
    generate()