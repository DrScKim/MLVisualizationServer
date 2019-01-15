
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def wine_data_load_n_split_train_test(ratio = 0.25):
    wine_data = load_wine()
    X_train, X_test, Y_train, Y_test = train_test_split(wine_data.data, wine_data.target, test_size=ratio)
    return (wine_data, X_train, X_test, Y_train, Y_test)
