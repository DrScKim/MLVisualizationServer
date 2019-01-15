from sklearn.linear_model import LogisticRegression
from MLExamples.util.dataLoader import *
from MLExamples.PreProcessing.Scaler import *


def l1_regularization():
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test(0.33)
    X_train_std, X_test_std = standarizer(X_train, X_test)
    regressor = LogisticRegression(penalty='l1', C=0.1)
    regressor.fit(X_train_std, Y_train)
    print('Training accuracy:', regressor.score(X_train_std, Y_train))
    print('Test accuracy:', regressor.score(X_test_std, Y_test))

if __name__ == "__main__":
    l1_regularization()