# Databricks notebook source
# MAGIC %md ### Test Repos - Workspace Experiment
# MAGIC 
# MAGIC Experiment: https://demo.cloud.databricks.com/#mlflow/experiments/12516221

# COMMAND ----------

#notebook = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
#dbutils.widgets.text("Experiment name", notebook)
#experiment_name = dbutils.widgets.get("Experiment name")
experiment_name = "/Users/andre.mesarovic@databricks.com/experiments/dbx-repo/Test_Workspace_Experiment"
experiment_name

# COMMAND ----------

import mlflow
client = mlflow.tracking.MlflowClient()
mlflow.set_experiment(experiment_name)

# COMMAND ----------

with mlflow.start_run() as run:
    mlflow.set_tag("greetings", "Hello Workspace Experiment - main branch")
    print("run_id:", run.info.run_id)
    print("experiment_id:", run.info.experiment_id)
    print("experiment_name:", client.get_experiment(run.info.experiment_id).name)

# COMMAND ----------

#commit = "d53dbeb2b40c46efec2607de6023693978700a38"
#client.set_tag(run.info.run_id, "mlflow.source.git.commit",commit)

# COMMAND ----------

host_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get("browserHostName").get()
uri = "https://{}/#mlflow/experiments/{}/runs/{}".format(host_name, run.info.experiment_id, run.info.run_id)
displayHTML("""<b>Run URI:</b> <a href="{}">{}</a>""".format(uri,uri))
uri = "https://{}/#mlflow/experiments/{}".format(host_name, run.info.experiment_id)
displayHTML("""<b>Experiment URI:</b> <a href="{}">{}</a>""".format(uri,uri))
