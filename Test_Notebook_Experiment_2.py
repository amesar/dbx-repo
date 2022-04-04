# Databricks notebook source
# MAGIC %md ## Test_Notebook_Experiment_2 - dev branch

# COMMAND ----------

import mlflow
client = mlflow.tracking.MlflowClient()

# COMMAND ----------

with mlflow.start_run(run_name="dev branch 2") as run:
    mlflow.set_tag("greetings", "Hello Notebook Experiment")
    print("run_id:", run.info.run_id)
    print("experiment_id:", run.info.experiment_id)
    print("experiment_name:", client.get_experiment(run.info.experiment_id).name)

# COMMAND ----------

client.set_tag(run.info.run_id, "mlflow.source.git.commit","foo")
client.set_tag(run.info.run_id, "mlflow.source.git.repoURL","bar")

# COMMAND ----------

run = client.get_run(run.info.run_id)
run.data.tags

# COMMAND ----------

host_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get("browserHostName").get()
uri = "https://{}/#mlflow/experiments/{}/runs/{}".format(host_name, run.info.experiment_id, run.info.run_id)
displayHTML("""<b>Run URI:</b> <a href="{}">{}</a>""".format(uri,uri))
uri = "https://{}/#mlflow/experiments/{}".format(host_name, run.info.experiment_id)
displayHTML("""<b>Experiment URI:</b> <a href="{}">{}</a>""".format(uri,uri))
