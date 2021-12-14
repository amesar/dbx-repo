# Databricks notebook source
# MAGIC %md ### Test Repos - Workspace Experiment

# COMMAND ----------

import mlflow
client = mlflow.tracking.MlflowClient()

experiment_name = "/Repos/andre.mesarovic@databricks.com/dbx-repo/My_Workspace_Experiment"
mlflow.set_experiment(experiment_name)


# COMMAND ----------

with mlflow.start_run() as run:
    mlflow.set_tag("greetings", "Hello Workspace Experiment")
    print("run_id:", run.info.run_id)
    print("experiment_id:", run.info.experiment_id)
    print("experiment_name:", client.get_experiment(run.info.experiment_id).name)

# COMMAND ----------

host_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get("browserHostName").get()
uri = "https://{}/#mlflow/experiments/{}".format(host_name, run.info.experiment_id)
displayHTML("""<b>Experiment URI:</b> <a href="{}">{}</a>""".format(uri,uri))

# COMMAND ----------


