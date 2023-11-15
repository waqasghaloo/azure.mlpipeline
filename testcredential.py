from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential


# Creating a client of Azure ML and loading configuration from config.json
ml_client =  client = MLClient.from_config(
       credential=DefaultAzureCredential(),
       file_name=r"azure.mlpipeline\config.json",
   )

print(ml_client)