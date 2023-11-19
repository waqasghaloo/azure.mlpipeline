import os
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import json




def construct_path(subdirectory = "src"):
    # Get the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the config file
    config_path = os.path.join(script_dir,subdirectory, "config.json")

    return config_path

configpath = construct_path()

def read_configjson(config_path, key = "workspace_name"):
    # Read the configuration from the JSON file
    # Read the contents of the JSON file as a string
    with open(config_path, "r") as file:
        config_json_string = file.read()

    # Parse the JSON string
    config_data = json.loads(config_json_string)
    # Access the values using the key
    workspace_name = config_data.get(key)

    return workspace_name


# Creating a client of Azure ML and loading configuration from config.json
ml_client = MLClient.from_config(
    # Reading DefaultAzureCredential is possible when 'azd auth login' is done
    credential = DefaultAzureCredential(),   
    path = construct_path()
   )

# Verify that the handle works correctly.  
# If you ge an error here, modify your SUBSCRIPTION, RESOURCE_GROUP, and WS_NAME in the previous cell.
ws = ml_client.workspaces.get(read_configjson(configpath))
print(ws.location,":", ws.resource_group)

