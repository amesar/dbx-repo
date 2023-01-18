# Databricks notebook source
# MAGIC %md ### Test Repos - Workspace Experiment - main branch
# MAGIC 
# MAGIC Experiment: 
# MAGIC * https://e2-demo-west.cloud.databricks.com/?o=2556758628403379#mlflow/experiments/263313384358022?
# MAGIC * https://demo.cloud.databricks.com/#mlflow/experiments/12516221

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

import time
now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
with mlflow.start_run(run_name="main branch - {now}") as run:
    mlflow.set_tag("greetings", "Hello Workspace Experiment - main branch")
    mlflow.set_tag("timestamp", now)
    mlflow.set_tag("version_mlflow", mlflow.__version__)
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("rmse", 0.789)
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
