# Databricks notebook source
import mlflow
client = mlflow.client.MlflowClient()
mlflow.__version__

# COMMAND ----------

import mlflow
run_id = "02e308f2170f4027b0f486152fb0360c"
client = mlflow.client.MlflowClient()
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

# COMMAND ----------

# MAGIC %md ### Delete Notebook Experiment
# MAGIC 
# MAGIC * Test_Notebook_Experiment_TestDelete
# MAGIC   * Cannot delete Repos notebook experiment - RestException: BAD_REQUEST: Deletion is not supported for this experiment.

# COMMAND ----------

# MAGIC %md #### Test_Notebook_Experiment_TestDelete

# COMMAND ----------

exp_name ="/Repos/andre.mesarovic@databricks.com/dbx-repo/Test_Notebook_Experiment_TestDelete"
exp = client.get_experiment_by_name(exp_name)
exp

# COMMAND ----------

client.delete_experiment(exp.experiment_id)

# COMMAND ----------

exp = client.get_experiment(exp.experiment_id)
exp

# COMMAND ----------

# MAGIC %md #### Test_Workspace_Experiment_TestDelete

# COMMAND ----------

exp_name = "/Users/andre.mesarovic@databricks.com/experiments/dbx-repo/Test_Workspace_Experiment_TestDelete"
exp = client.get_experiment_by_name(exp_name)
exp

# COMMAND ----------

client.delete_experiment(exp.experiment_id)

# COMMAND ----------

exp = client.get_experiment(exp.experiment_id)
exp.lifecycle_stage, exp

# COMMAND ----------


