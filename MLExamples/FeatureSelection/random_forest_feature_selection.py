

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
from MLExamples.util.train_test_module import *
from MLExamples.util.dataLoader import *
from sklearn.neighbors import KNeighborsClassifier
from MLExamples.PreProcessing.Scaler import standarizer

def run(htmlWrite=False, visualizerPath='', n_tree_estims=1000):
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test()
    forest = RandomForestClassifier(n_estimators=n_tree_estims, random_state=0, n_jobs=-1)
    forest.fit(X_train, Y_train)
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    _importances = [importances[indices[f]] for f in range(X_train.shape[1])]
    for f in range(X_train.shape[1]):
        print("%2d) %-*s %f" % ( f + 1, 30,
                                 wine_data.feature_names[f],
                                 _importances[f]))
    if (htmlWrite==True):
        import Visualizer.VisualizerUtil as vis
        layout = dict()
        layout['title']='Feature Importances'
        layout['yaxis']=dict(range=[0,0.2])
        _path = None
        if len(visualizerPath) != 0:
            _path=visualizerPath
        vis.genPlotly1DBarChart(labels=wine_data.feature_names, layout=layout, data=_importances, path=_path, width_size=0.8)
    return forest



def train_all_features():
    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test()

    pass

def visualizePreRecallByParams(n_estims=1000, n=5):

    wine_data, X_train, X_test, Y_train, Y_test = wine_data_load_n_split_train_test(0.25)
    X_train, X_test = standarizer(X_train, X_test)
    KNN = KNeighborsClassifier(n_neighbors=n)
    train_calc_time(KNN, X_train, Y_train)
    y_pred = KNN.predict(X_test)
    all_feature_result = precision_recall_fscore_support(Y_test, y_pred, average='weighted')

    print("without Selection: total Num of Featurs: %d\nprecision: %f, recall: %f, f1-score: %f"
          % (X_train.shape[1], all_feature_result[0], all_feature_result[1], all_feature_result[2]))

    thr_labels = [0.01, 0.02, 0.05, 0.08, 0.1, 0.13, 0.15]
    allFeat = dict()
    selected = dict()
    allFeat['prec'] = [ all_feature_result[0]] *len(thr_labels)
    allFeat['rec'] =  [ all_feature_result[1]] *len(thr_labels)
    allFeat['f1'] =  [ all_feature_result[2]] *len(thr_labels)
    selected['prec']=list()
    selected['rec']=list()
    selected['f1']=list()

    for thr in thr_labels:
        from sklearn.feature_selection import SelectFromModel
        forest = RandomForestClassifier(n_estimators=n_estims, random_state=0, n_jobs=-1)
        forest.fit(X_train, Y_train)
        sfm = SelectFromModel(forest, threshold=thr)
        sfm.fit(X_train, Y_train)
        X_selected_train = sfm.transform(X_train)
        X_selected_test = sfm.transform(X_test)
        model = KNeighborsClassifier(n_neighbors=n)#RandomForestClassifier(n_estimators=n_estims, random_state=0, n_jobs=-1)
        selected_feature_result = train_test_selected_features(model, X_selected_train, X_selected_test, Y_train, Y_test, True)

        selected['prec'].append(selected_feature_result[0])
        selected['rec'].append(selected_feature_result[1])
        selected['f1'].append(selected_feature_result[2])

    import Visualizer.VisualizerUtil as vis

    vis.gen_params_prec_recall_curve(thr_labels, allFeat['prec'], selected['prec'],
                                         allFeat['rec'], selected['rec'], allFeat['f1'], selected['f1'])

if __name__ == "__main__":
    #run(False)
    visualizePreRecallByParams(250,5)
