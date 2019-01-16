from sklearn.decomposition import KernelPCA
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from util.durationLog import *
from MLExamples.util.dataLoader import *
from MLExamples.FeatureSelection.random_forest_feature_selection import *
from MLExamples.util.train_test_module import *

def visualizePreRecallByParams(n_estims=1000, n=5):
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test(0.25)
    X_train, X_test = standarizer(X_train, X_test)
    KNN = KNeighborsClassifier(n_neighbors=n)
    train_calc_time(KNN, X_train, Y_train)
    y_pred = KNN.predict(X_test)
    all_feature_result = precision_recall_fscore_support(Y_test, y_pred, average='weighted')

    print("without Selection: total Num of Featurs: %d\nprecision: %f, recall: %f, f1-score: %f"
          % (X_train.shape[1], all_feature_result[0], all_feature_result[1], all_feature_result[2]))

    thr_labels = [2*i+1 for i in range(len(wine_data.feature_names)>>1)]
    allFeat = dict()
    selected = dict()
    allFeat['prec'] = [ all_feature_result[0]] * len(thr_labels)
    allFeat['rec'] =  [ all_feature_result[1]] * len(thr_labels)
    allFeat['f1'] =  [ all_feature_result[2]] * len(thr_labels)
    selected['prec']=list()
    selected['rec']=list()
    selected['f1']=list()

    for thr in thr_labels:
        print(thr)

        scikit_pca = KernelPCA(kernel='poly', n_components=min(len(wine_data.feature_names), thr))
        X_spca = scikit_pca.fit(wine_data.data)
        X_selected_train = X_spca.transform(X_train)
        X_selected_test = X_spca.transform(X_test)
        model = KNeighborsClassifier(n_neighbors=n)
        selected_feature_result = train_test_selected_features(model, X_selected_train, X_selected_test, Y_train, Y_test, True)
        selected['prec'].append(selected_feature_result[0])
        selected['rec'].append(selected_feature_result[1])
        selected['f1'].append(selected_feature_result[2])

    import Visualizer.VisualizerUtil as vis

    vis.gen_params_prec_recall_curve(thr_labels, allFeat['prec'], selected['prec'],
                                         allFeat['rec'], selected['rec'], allFeat['f1'], selected['f1'],
                                     _filename=vis.TEMPLATE_DIR+'featureEngineering/prec_rec_by_pca.html')

if __name__ == "__main__":
    visualizePreRecallByParams(250,5)