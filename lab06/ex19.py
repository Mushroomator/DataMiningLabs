import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as scn; scn.set()
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

dataset = load_iris()
X = dataset["data"]
y = dataset["target"]
features = np.array(["sepallength","sepalwidth","petallength","petalwidth"])
df = pd.DataFrame(X, columns=features)

n_clusters = 3
model = KMeans(n_clusters=n_clusters)
model.fit(X)
labels = model.labels_
centres = model.cluster_centers_
print(labels)
print(y)

bild = plt.figure(num="Irisdaten",figsize=(11,5))
inhalt1 = bild.add_subplot(121)         # Linkes Bild
inhalt1.scatter(df[labels==0].petallength, df[labels==0].petalwidth, c='b', s=25, label="Cluster1")
inhalt1.scatter(df[labels==1].petallength, df[labels==1].petalwidth, c='y', s=25, label="Cluster2")
inhalt1.scatter(df[labels==2].petallength, df[labels==2].petalwidth, c='g', s=25, label="Cluster3")
inhalt1.scatter(centres[:,2], centres[:, 3], c="k", s=60, label="Centers")
inhalt1.set_title("Mit k-Means berechnet")
inhalt1.axis([0,8,0,4])
inhalt1.legend()
inhalt1.set_xlabel("petallength")
inhalt1.set_ylabel("petalwidth")

inhalt2 = bild.add_subplot(122)         # Rechtes Bild
inhalt2.scatter(df[y==0].petallength, df[y==0].petalwidth, c='b', s=25, label="Setosa")
inhalt2.scatter(df[y==1].petallength, df[y==1].petalwidth, c='y', s=25, label="Versicolor")
inhalt2.scatter(df[y==2].petallength, df[y==2].petalwidth, c='g', s=25, label="Virginica")
inhalt2.set_title("Originaldaten")
inhalt2.axis([0,8,0,4])
inhalt2.legend()
inhalt2.set_xlabel("petallength")
inhalt2.set_ylabel("petalwidth")
plt.show()