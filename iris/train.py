import click
import mlflow
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics 
from data_prep import get_data

print("Versions:")
print("  MLflow Version:", mlflow.__version__)
print("  Sklearn Version:", sklearn.__version__)
print("  MLflow Tracking URI:", mlflow.get_tracking_uri())

def train(experiment_name=None, model_name=None, max_depth=5, data_path=None):
    X_train, X_test, y_train, y_test = get_data(data_path)
    if experiment_name:
        mlflow.set_experiment(experiment_name)
    with mlflow.start_run() as run: 
        print("run_id:", run.info.run_id)
        mlflow.set_tag("mlflow_version",mlflow.__version__)
        mlflow.log_param("max_depth",max_depth)
        model = DecisionTreeClassifier(max_depth=max_depth)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print("Predictions:",predictions)
        accuracy_score = metrics.accuracy_score(y_test, predictions)
        print("accuracy_score:",accuracy_score)
        mlflow.log_metric("accuracy_score",accuracy_score)
        mlflow.sklearn.log_model(model, "sklearn-model", registered_model_name=model_name)
        return accuracy_score

@click.command()
@click.option("--experiment-name", help="Experiment name.", default=None, type=str)
@click.option("--data-path", help="Data path.", default=None, type=str)
@click.option("--model-name", help="Registered model name.", default=None, type=str)
@click.option("--max-depth", help="Max depth parameter.", default=5, type=int)

def main(experiment_name, data_path, model_name, max_depth):
    print("Options:")
    for k,v in locals().items():
        print(f"  {k}: {v}")
    return train(experiment_name, model_name, max_depth, data_path)

if __name__ == "__main__":
    main()
