from util.durationLog import *
from sklearn.metrics import precision_recall_fscore_support

@calc_duration
def train_calc_time(model, train_data, train_label):
    model.fit(train_data, train_label)

def train(model, train_data, train_label):
    model.fit(train_data, train_label)

def train_test_selected_features(model, X_selected_train, X_selected_test, Y_train, Y_test, isConsoleDubug=True, isDumpOperationTime=True):
    if isDumpOperationTime == True:
        train_calc_time(model, X_selected_train, Y_train)
    else:
        train(model, X_selected_train, Y_train)
    y_selected_pred = model.predict(X_selected_test)
    selected_feature_result = precision_recall_fscore_support(Y_test, y_selected_pred, average='weighted')
    if ( isConsoleDubug == True):
        print("with Selection: total Num of Featurs: %d\nprecision: %f, recall: %f, f1-score: %f"
              % (X_selected_train.shape[1], selected_feature_result[0], selected_feature_result[1], selected_feature_result[2]))

    return selected_feature_result
