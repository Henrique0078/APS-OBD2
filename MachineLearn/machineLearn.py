from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, 'dataset', 'O2_dataset.pkl')
with open(dataset_path, 'rb') as f:
    x_train, y_train, x_test, y_test = pickle.load(f)


#Treina a IA
async def train_IA():
    svm_model = SVC(random_state=1)
    svm_model.fit(x_train, y_train)
    predict = svm_model.predict(x_test)
    print(accuracy_score(predict, y_test))
    return predict.tolist()
