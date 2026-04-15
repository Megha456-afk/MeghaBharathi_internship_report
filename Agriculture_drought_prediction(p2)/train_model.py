import pandas as pd
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("dataset/drought_data.csv")

X = data[['rainfall','temperature','humidity','soil_moisture','wind_speed']]
y = data['drought']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

def metrics(y_true, y_pred):
    return [
        accuracy_score(y_true, y_pred),
        precision_score(y_true, y_pred),
        recall_score(y_true, y_pred),
        f1_score(y_true, y_pred)
    ]

rf_metrics = metrics(y_test, rf_pred)
lr_metrics = metrics(y_test, lr_pred)

print("RF:", rf_metrics)
print("LR:", lr_metrics)

if rf_metrics[0] > lr_metrics[0]:
    joblib.dump(rf, "model.pkl")
    model_info = {"model": "Random Forest", "accuracy": rf_metrics[0]}
else:
    joblib.dump(lr, "model.pkl")
    model_info = {"model": "Logistic Regression", "accuracy": lr_metrics[0]}

with open("model_info.json", "w") as f:
    json.dump(model_info, f)
import matplotlib.pyplot as plt

importances = rf.feature_importances_
features = X.columns

plt.bar(features, importances)
plt.title("Feature Importance")
plt.xticks(rotation=45)
plt.show()