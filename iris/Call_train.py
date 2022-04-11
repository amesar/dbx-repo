# Databricks notebook source
# MAGIC %md ## Call Repo python files

# COMMAND ----------

 exp_name = "/Users/andre.mesarovic@databricks.com/experiments/iris-dbx-repo"

# COMMAND ----------

# MAGIC %md #### Call non-autolog training

# COMMAND ----------

 import train
 train.train(exp_name)

# COMMAND ----------

# MAGIC %md #### Call autolog training

# COMMAND ----------

 import autolog_train
 exp_name = "/Users/andre.mesarovic@databricks.com/experiments/iris-dbx-repo"
 autolog_train.train(exp_name)

# COMMAND ----------

# MAGIC %md #### Call non-autolog training from click main
# MAGIC 
# MAGIC Fails due to internal click probllem

# COMMAND ----------

import train
train.main(["--experiment-name", exp_name])
