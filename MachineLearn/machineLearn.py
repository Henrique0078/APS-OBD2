from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import pickle
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, 'dataset', 'O2_dataset.pkl')
with open(dataset_path, 'rb') as f:
    x_train, y_train, x_test, y_test = pickle.load(f)

svm_model = SVC(random_state=1)
svm_model.fit(x_train, y_train)
predict = svm_model.predict(x_test)
print(accuracy_score(predict, y_test))

async def predict_IA(dados):
    result = svm_model.predict(dados)
    predict = np.append(predict, result)
    return result.tolist()
