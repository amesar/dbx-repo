import click
import mlflow
import sklearn
from sklearn.tree import DecisionTreeClassifier
from data_prep import get_data

print("Versions:")
print("  MLflow Version:", mlflow.__version__)
print("  Sklearn Version:", sklearn.__version__)
print("  MLflow Tracking URI:", mlflow.get_tracking_uri())

def train(experiment_name=None, max_depth=5, data_path=None):
    if experiment_name:
        mlflow.set_experiment(experiment_name)
    mlflow.sklearn.autolog()
    X_train, X_test, y_train, _ = get_data(data_path)
    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Predictions:",predictions)


@click.command()
@click.option("--experiment-name", help="Experiment name.", default=None, type=str)
@click.option("--data-path", help="Data path.", default=None, type=str)
@click.option("--max-depth", help="Max depth parameter.", default=5, type=int)

def main(experiment_name, data_path, max_depth):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    train(experiment_name, max_depth, data_path)

if __name__ == "__main__":
    main()
