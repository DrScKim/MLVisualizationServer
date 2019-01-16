from sklearn.linear_model import LogisticRegression
from MLExamples.util.dataLoader import *
from MLExamples.PreProcessing.Scaler import *

#if you don't want to look at Future warning, uncomment below two line,
#please remind that if you update scikit-learn over 0.22, you'll have to change logistic regression
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def l1_regularization():
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test(0.33)
    X_train_std, X_test_std = standarizer(X_train, X_test)
    regressor = LogisticRegression(penalty='l1', C=0.1)
    regressor.fit(X_train_std, Y_train)
    print('Training accuracy:', regressor.score(X_train_std, Y_train))
    print('Test accuracy:', regressor.score(X_test_std, Y_test))
    print('\n###intercept###')
    print(regressor.intercept_)
    print('\n###coefficients###')
    print(regressor.coef_)
if __name__ == "__main__":
    l1_regularization()