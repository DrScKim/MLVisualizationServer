
from MLExamples.util.dataLoader import *
from MLExamples.util.train_test_module import *
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def pipeline():
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    breast_cancer_data, X_train, X_test, Y_train, Y_test = breast_cancer_load_n_split_train_test()

    pipe_knn5 = Pipeline(
        [('scl', StandardScaler()),
         ('clf',KNeighborsClassifier(n_neighbors=5))
         ],
    )
    pipe_knn3 = Pipeline(
        [('scl', StandardScaler()),
         ('clf', KNeighborsClassifier(n_neighbors=3))
         ],
    )
    pipe_knn7 = Pipeline(
        [('scl', StandardScaler()),
         ('clf', KNeighborsClassifier(n_neighbors=7))
         ],
    )
    pipe_knn = Pipeline(
        [('scl', StandardScaler()),
         ('pca', PCA(n_components=2)),
         ('clf', KNeighborsClassifier(n_neighbors=5))
         ],
    )
    pipe_knn_withoutScaling = Pipeline(
        [('pca', PCA(n_components=2)),
         ('clf',KNeighborsClassifier(n_neighbors=5))
         ],
    )
    pipe_knn_withoutScaling_no_pca = Pipeline(
        [('clf', KNeighborsClassifier(n_neighbors=5))
         ],
    )
    pipe_lr = Pipeline(
        [('scl', StandardScaler()),
         ('pca', PCA(n_components=2)),
         ('clf', LogisticRegression(random_state=1))
         ],
    )

    print("pipeline test, K=5, PCA, StandardScaling")
    train_test_selected_features(pipe_knn, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("pipeline test, neighbour = 3")
    train_test_selected_features(pipe_knn3, X_train,  X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("pipeline test, neighbour = 5")
    train_test_selected_features(pipe_knn5, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("pipeline test, neighbour = 7")
    train_test_selected_features(pipe_knn7, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("except scaling test")
    train_test_selected_features(pipe_knn_withoutScaling, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("without dim redunction test")
    train_test_selected_features(pipe_knn_withoutScaling_no_pca, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)
    print("pipeline test for Logistic Regression")
    train_test_selected_features(pipe_lr, X_train, X_test, Y_train, Y_test,
                                 isDumpOperationTime=False)


#    breast_cancer_data, data_train_set, data_test_set, label_train_set, label_test_set = breast_cancer_load_K_fold()

if __name__ == "__main__":
    pipeline()



