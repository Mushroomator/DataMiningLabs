import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

dataset = load_iris()
X = dataset["data"]
y = dataset["target"]

cols = np.array(["sepallength", "sepalwidth", "petallength", "petalwidth"])
df = pd.DataFrame(X, columns=cols)

zufallsstrom = 14
X_train, X_test = train_test_split(df, random_state=zufallsstrom)
print(f"Trainingsdaten {X_train.shape}]\n", X_train)
print(f"Testdaten {X_test.shape}\n", X_test)

model_nb = GaussianNB()
model_nb.fit(X, y)
y_prediction = model_nb.predict(X_test)
print("Original Daten:\n",y)
print("Vorhersage Naive Bayes:\n", y_prediction)