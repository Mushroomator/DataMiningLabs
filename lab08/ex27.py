import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

raw = pd.read_csv("weather.csv", sep=";")

def quantify(column_name):
    map = {val: i for i, val in enumerate(raw[column_name].drop_duplicates().values)}
    raw[column_name] = [map[val] for val in raw[column_name]]


quantify("Decision")
quantify("Weather")
quantify("Parents")
quantify("Money")

X = raw.iloc[:,1:-1]
y = raw["Decision"]
print(X)
model = tree.DecisionTreeClassifier()
model.fit(X, y)

plt.figure(num="Tree", figsize=(10, 5))
tree.plot_tree(model, feature_names=X.columns, filled=True, rounded=True, fontsize=6)
plt.show()

