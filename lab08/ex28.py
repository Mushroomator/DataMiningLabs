import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, recall_score, precision_score

diabtetes_data = pd.read_csv("diabetes_dataset.csv")
y = diabtetes_data["Outcome"]
X = diabtetes_data.iloc[:,:-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=16)

# min_sample_split: 0.25, max_features: 7
model = DecisionTreeClassifier(criterion="entropy",min_samples_split=0.25, max_features=5)
model.fit(X_train, y_train)

# plt.figure(num="Tree", figsize=(15, 10))
# plot_tree(model)
# plt.show()

y_predict = model.predict(X_test)
print(f"Korrektheit (Accuracy): {accuracy_score(y_test, y_predict)}")
print(f"Treffsicherheit (Recall): {recall_score(y_test, y_predict)}")
print(f"Präzision (Precision): {precision_score(y_test, y_predict)}")