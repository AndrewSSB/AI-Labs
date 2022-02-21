y_pred = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
y_true = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

def accuracy_score(y_true, y_pred):
    acuratete = 0
    for i in range(len(y_pred)):
        acuratete += acuratete + (y_pred[i] == y_true[i])
    acuratete = acuratete/len(y_pred)

def precision_recall_score(y_true, y_pred):
    tp = 0
    fp = 0
    fn = 0
    for i in range(len(y_true)):
        if (y_true[i] == y_pred[i] and y_true == 1):
            tp = tp+1
        elif (y_true[i] == 0 and y_pred == 1):
            fp = fp+1
        elif(y_true[i] == 1 and y_pred == 0):
            fn = fn+1

    precizie = tp/(tp + fp)
    recall = tp/(tp + fn)
    return precizie, recall

def mse(y_true, y_pred):
    mse = 0
    for i in range(len(y_true)):
        mse = mse + (y_pred[i] - y_true)**2
    mse = mse/4

    return mse

def mae(y_true, y_pred):
    mae = 0
    for i in range(len(y_pred)):
        mae = abs(y_pred - y_true)
    return mae