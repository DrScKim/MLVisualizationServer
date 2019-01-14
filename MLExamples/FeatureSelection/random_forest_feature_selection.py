
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
import numpy as np

def data_load_n_split_train_test(ratio = 0.25):
    wine_data = load_wine()
    X_train, X_test, Y_train, Y_test = train_test_split(wine_data.data, wine_data.target, test_size=ratio)
    return (wine_data, X_train, X_test, Y_train, Y_test)

def run(htmlWrite=False, visualizerPath='', n_tree_estims=1000):
    wine_data, X_train, X_test, Y_train, Y_test = data_load_n_split_train_test()
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
    wine_data, X_train, X_test, Y_train, Y_test = data_load_n_split_train_test()

    pass

def train_test_selected_features(model, X_train, X_test, Y_train, Y_test, n_estims=1000, thr = 0.1, isConsoleDubug=True):
    from sklearn.feature_selection import SelectFromModel
    sfm = SelectFromModel(model, threshold=thr)
    sfm.fit(X_train, Y_train)
    X_selected_train = sfm.transform(X_train)
    X_selected_test = sfm.transform(X_test)
    selectedForest = RandomForestClassifier(n_estimators=n_estims, random_state=0, n_jobs=-1)

    selectedForest.fit(X_selected_train, Y_train)
    y_selected_pred = selectedForest.predict(X_selected_test)

    selected_feature_result = precision_recall_fscore_support(Y_test, y_selected_pred, average='weighted')
    if ( isConsoleDubug == True):
        print("with Selection: total Num of Featurs: %d\nprecision: %f, recall: %f, f1-score: %f"
              % (X_selected_train.shape[1], selected_feature_result[0], selected_feature_result[1], selected_feature_result[2]))

    return selected_feature_result




def visualizePreRecallByParams(n_estims=1000):

    wine_data, X_train, X_test, Y_train, Y_test = data_load_n_split_train_test(0.5)
    forest = RandomForestClassifier(n_estimators=n_estims, random_state=0, n_jobs=-1)
    forest.fit(X_train, Y_train)
    y_pred = forest.predict(X_test)
    all_feature_result = precision_recall_fscore_support(Y_test, y_pred, average='weighted')
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    _importances = [importances[indices[f]] for f in range(X_train.shape[1])]
    for f in range(X_train.shape[1]):
        print("%2d) %-*s %f" % (f + 1, 30,
                                wine_data.feature_names[f],
                                _importances[f]))
    print("without Selection: total Num of Featurs: %d\nprecision: %f, recall: %f, f1-score: %f"
          % (X_train.shape[1], all_feature_result[0], all_feature_result[1], all_feature_result[2]))

    thr_labels = [0.01, 0.02, 0.05, 0.08, 0.1, 0.13, 0.15]
    allFeat = dict()
    selected = dict()
    allFeat['prec'] = list()
    allFeat['rec'] = list()
    allFeat['f1'] = list()
    selected['prec']=list()
    selected['rec']=list()
    selected['f1']=list()

    for thr in thr_labels:
        selected_feature_result = train_test_selected_features(forest, X_train, X_test, Y_train, Y_test, n_estims, thr, False)
        allFeat['prec'].append(all_feature_result[0])
        allFeat['rec'].append(all_feature_result[1])
        allFeat['f1'].append(all_feature_result[2])
        selected['prec'].append(selected_feature_result[0])
        selected['rec'].append(selected_feature_result[1])
        selected['f1'].append(selected_feature_result[2])

    import Visualizer.VisualizerUtil as vis

    vis.gen_params_prec_recall_curve(thr_labels, allFeat['prec'], selected['prec'],
                                         allFeat['rec'], selected['rec'], allFeat['f1'], selected['f1'])

run(True)
#visualizePreRecallByParams()
