# Databricks notebook source
print("Test Repo notebook")

# COMMAND ----------

import python_script
python_script.funk()

# COMMAND ----------

from dir import python_script
python_script.funk()

# COMMAND ----------

import json
path = "data.json"
with open(path, "r") as f:
    dct = json.loads(f.read())
dct

# COMMAND ----------


