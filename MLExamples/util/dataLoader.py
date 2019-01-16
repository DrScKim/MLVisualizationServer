
from sklearn.datasets import load_wine
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

def wine_data_load_n_split_train_test(ratio = 0.25):
    wine_data = load_wine()
    X_train, X_test, Y_train, Y_test = train_test_split(wine_data.data, wine_data.target, test_size=ratio)
    return (wine_data, X_train, X_test, Y_train, Y_test)

def breast_cancer_load_n_split_train_test(ratio = 0.25):
    breast_cancer_data = load_breast_cancer()
    X_train, X_test, Y_train, Y_test = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=ratio)
    return (breast_cancer_data, X_train, X_test, Y_train, Y_test)


def breast_cancer_load_K_fold(K=5):
    breast_cancer_data = load_breast_cancer()
    kfold = KFold(K, shuffle=True, random_state=0)
    data_train_set = []
    data_test_set = []
    label_train_set = []
    label_test_set = []
    for i, (index_train, index_test) in enumerate(kfold.split(breast_cancer_data.data)):
        data_train_set.append(breast_cancer_data.data[index_train.tolist()])
        data_test_set.append(breast_cancer_data.data[index_test.tolist()])
        label_train_set.append(breast_cancer_data.target[index_train.tolist()])
        label_test_set.append(breast_cancer_data.target[index_test.tolist()])

    return breast_cancer_data, data_train_set, data_test_set, label_train_set, label_test_set






