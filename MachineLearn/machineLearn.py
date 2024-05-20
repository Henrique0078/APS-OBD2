from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc, precision_recall_curve
import numpy as np
import pickle
import os
import json

# Carregando os dados
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, 'dataset', 'O2_dataset.pkl')
with open(dataset_path, 'rb') as f:
    x_train, y_train, x_test, y_test = pickle.load(f)

# Inicializando o modelo SVC com probability=True
svm_model = SVC(probability=True, random_state=42)
svm_model.fit(x_train, y_train)

# Fazendo previsões e calculando probabilidades
predict = svm_model.predict(x_test)
predict_proba = svm_model.predict_proba(x_test)[:, 1]

# Calcular métricas
accuracy = accuracy_score(y_test, predict)
conf_matrix = confusion_matrix(y_test, predict)
fpr, tpr, _ = roc_curve(y_test, predict_proba)
roc_auc = auc(fpr, tpr)
precision, recall, _ = precision_recall_curve(y_test, predict_proba)

# Salvar métricas em um arquivo JSON
metrics = {
    "accuracy": accuracy,
    "confusion_matrix": conf_matrix.tolist(),
    "roc_curve": {
        "fpr": fpr.tolist(),
        "tpr": tpr.tolist(),
        "auc": roc_auc
    },
    "precision_recall": {
        "precision": precision.tolist(),
        "recall": recall.tolist()
    }
}

metrics_path = os.path.join(current_dir, 'metrics.json')
with open(metrics_path, 'w') as f:
    json.dump(metrics, f)

print(f"Accuracy: {accuracy}")

# Definindo a função predict_IA
async def predict_IA(dados):
    result = svm_model.predict(dados)
    return result.tolist()

# Certificando-se de exportar as funções necessárias
__all__ = ['predict_IA', 'predict', 'x_test']
