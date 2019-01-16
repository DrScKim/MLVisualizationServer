


from sklearn.decomposition import KernelPCA
from sklearn.linear_model import LogisticRegression
from MLExamples.util.dataLoader import *
from Visualizer.importPlotly import *
from MLExamples.PreProcessing.Scaler import *
import numpy as np
from Visualizer.VisualizerUtil import *
from sklearn.decomposition import LatentDirichletAllocation


def dotPlot(X, y, classifier, filepath, resolution=0.02):
    markers = [0, 1,2, 3,4]
    colors = ['red', 'blue', 'lightgreen', 'gray', 'cyan']

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    layout = go.Layout(
        title='Feature Visualization',
        xaxis=dict(title='x1', range=[xx1.min(), xx1.max()]),
        yaxis=dict(title='x2', range=[xx2.min(), xx2.max()])
    )
    genPlotlyDotPlot(X, y, _layout=layout, contour=z, _filename=filepath, _markers=markers, _colors=colors)

def plotPointsByPCA(X_train, X_test, Y_train, Y_test, filepath):

    pca = KernelPCA(n_components=2)
    lr = LogisticRegression()
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.fit_transform(X_test)
    lr.fit(X_train_pca, Y_train)

    dotPlot(X_train_pca, Y_train, lr, filepath)

def plotPointsByLDA(X_train, X_test, Y_train, Y_test, feature_names):
    lda = LatentDirichletAllocation(n_components=2)
    lr = LogisticRegression()
    X_train_lda = lda.fit_transform(X_train, Y_train)
    X_test_lda = lda.fit_transform(X_test, Y_test)
    lr.fit(X_train_lda, Y_train)

    dotPlot(X_train_lda, Y_train, lr)




def testPCA():
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test()
    X_train_std, X_test_std = standarizer(X_train, X_test)
    plotPointsByPCA(X_train_std, X_test_std, Y_train, Y_test, TEMPLATE_DIR+'featureEngineering/PCA.html')

def testLDA():
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test()
    X_train_std, X_test_std = standarizer(X_train, X_test)
    plotPointsByPCA(X_train_std, X_test_std, Y_train, Y_test, TEMPLATE_DIR+'featureEngineering/LDA.html')


if __name__ == "__main__":
    testPCA()
    testLDA()
