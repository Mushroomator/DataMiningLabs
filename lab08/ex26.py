import pandas as pd
import numpy as np

# Read data
X = pd.read_csv("weather.csv", sep=";")

def gini_for_column(column_name, unq_decisions):
    """Calculate Gini-index for a column with given

    :param column_name: column name
    :type column_name: list of str
    :param unq_decisions:
    :return:
    """
    unq_vals = X[column_name].drop_duplicates().values
    ginis = dict()
    for uval in unq_vals:
        val_tab = X[X[column_name] == uval]
        total_no = val_tab.shape[0]
        sum = 0;
        for dec in unq_decisions:
            featureWitDec = val_tab[val_tab["Decision"] == dec]
            noFeaturesWitDec = featureWitDec.shape[0]
            p = noFeaturesWitDec / total_no
            sum += p ** 2
        gini = 1 - sum
        ginis[uval] = gini
    return ginis

def calc_gini(df, classifier_col):
    """
    Compute gini index.

    :param df: Dataframe with weekend data
    :type df: pd.DataFrame
    :return:
    """
    uniqueDecisions = X[classifier_col].drop_duplicates().values
    for col in df.columns:
        ginis = gini_for_column(col, uniqueDecisions)
        print(ginis)

calc_gini(X, "Decision")