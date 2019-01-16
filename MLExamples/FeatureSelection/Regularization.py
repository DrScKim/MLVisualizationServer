from sklearn.linear_model import LogisticRegression
from MLExamples.util.dataLoader import *
from MLExamples.PreProcessing.Scaler import *
from Visualizer.VisualizerUtil import *
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

def f():
    import numpy as np
    colors = ['blue', 'green', 'red', 'cyan',
              'magenta', 'yellow', 'black',
              'pink', 'lightgreen', 'lightblue',
              'gray', 'indigo', 'orange']
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test(0.33)
    weights = []
    params = []
    X_train_std, X_test_std = standarizer(X_train, X_test)
    xaxisdata = []
    #for c in np.arange(-5,6).astype(float):
    for c in range(-5,6):
        xaxisdata.append(c)
        param = 10**c
        regressor = LogisticRegression(penalty='l1', C=param, random_state=0)
        regressor.fit(X_train_std, Y_train)
        weights.append(regressor.coef_[1])
        print(regressor.coef_[1])
        params.append(param)
    Tweights = []
    weights = np.array(weights)
    for column, color in zip(range(weights.shape[1]), colors):
        Tweights.append(weights[:, column])


    layout = go.Layout(
        title = 'L1 Regulrization',
        xaxis = dict(title = '10^x'),
        yaxis = dict(title = 'weight coeeficient', range = [-25,10])
    )
    genPlotlyMultiLineChart(xaxisdata, Tweights, _layout=layout, _filename=BASIC_LINE_CHART_PATH, colors=colors, names=wine_data.feature_names)

if __name__ == "__main__":
    #l1_regularization()
    f()