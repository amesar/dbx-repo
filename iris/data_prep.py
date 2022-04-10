import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

def get_data(data_path):
    if not data_path:
        dataset = datasets.load_iris()
        X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.3)
    else:
        df = pd.read_csv(data_path)
        train, test = train_test_split(df, test_size=0.3, random_state=42)
        col_label = "species"
        X_train = train.drop([col_label], axis=1)
        X_test = test.drop([col_label], axis=1)
        y_train = train[[col_label]]
        y_test = test[[col_label]]
    return X_train, X_test, y_train, y_test

