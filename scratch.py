# Databricks notebook source
import mlflow
run_id = "02e308f2170f4027b0f486152fb0360c"
client = mlflow.tracking.MlflowClient()
client.set_tag(run_id,"foo","bar")
run = mlflow.get_run(run_id)
run.data.tags

# COMMAND ----------

commit = "d53dbeb2b40c46efec2607de6023693978700a38"
client.set_tag(run_id,"mlflow.source.git.commit",commit)

repo_url = "https://github.com/amesar/dbx-repo"
client.set_tag(run_id,"mlflow.source.git.repoURL", repo_url)

run = mlflow.get_run(run_id)
run.data.tags

# COMMAND ----------

#client.set_tag(run_id,"mlflow.databricks.notebookRevisionID","2021")
#run = mlflow.get_run(run_id)
#run.data.tags
