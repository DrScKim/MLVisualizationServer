from MLExamples.util.dataLoader import *
from MLExamples.util.train_test_module import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
def standarizer(X_train, X_test):
    stdsc = StandardScaler()
    X_train_std = stdsc.fit_transform(X_train)
    X_test_std = stdsc.fit_transform(X_test)
    return X_train_std, X_test_std

def minmax_normalizer(X_train, X_test):
    minmax = MinMaxScaler()
    X_train_std = minmax.fit_transform(X_train)
    X_test_std = minmax.fit_transform(X_test)
    return X_train_std, X_test_std

def test_standarizer():
    from sklearn.neighbors.classification import KNeighborsClassifier
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test()

    KNN = KNeighborsClassifier(n_neighbors=5)
    print('basic input')
    train_test_selected_features(KNN, X_train, X_test, Y_train, Y_test, isDumpOperationTime=False)
    X_train_std, X_test_std = standarizer(X_train, X_test)
    print('standarization')
    train_test_selected_features(KNN, X_train_std, X_test_std, Y_train, Y_test, isDumpOperationTime=False)
    X_train_norm, X_test_norm = minmax_normalizer(X_train, X_test)
    print('min max norm')
    train_test_selected_features(KNN, X_train_norm, X_test_norm, Y_train, Y_test, isDumpOperationTime=False)


if __name__ == "__main__":
    #test_removeRow_containNaN(EXAMPLE_DATA)
    #test_impute_NaN(EXAMPLE_DATA)
    test_standarizer()
