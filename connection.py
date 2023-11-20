import os
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import json


def construct_path(subdirectory = "src"):
    """
    Constructs the absolute path to the config file.

    Args:
        subdirectory (str, optional): The subdirectory within the script's directory. Defaults to "src".

    Returns:
        str: The absolute path to the config file.
    """
    # Get the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the config file
    config_path = os.path.join(script_dir, subdirectory, "config.json")

    return config_path


import json

def read_configjson(config_path, key="workspace_name"):
    """
    Read the configuration from the JSON file and return the value associated with the given key.

    Parameters:
    config_path (str): The path to the JSON file.
    key (str, optional): The key to access the value in the JSON file. Defaults to "workspace_name".

    Returns:
    str: The value associated with the given key in the JSON file.
    """
    # Read the contents of the JSON file as a string
    with open(config_path, "r") as file:
        config_json_string = file.read()

    # Parse the JSON string
    config_data = json.loads(config_json_string)
    # Access the values using the key
    workspace_name = config_data.get(key)

    return workspace_name


# Creating a client of Azure ML and loading configuration from config.json
#  Creating MLClient will not connect to the workspace. The client initialization is lazy,
#  it will wait for the first time it needs to make a call (this will happen in the next code cell)

def create_ml_client():
    """
    Creates a client of Azure ML and loads configuration from config.json.

    Returns:
        MLClient: The client of Azure ML.
    """
    # Construct the path to the config file
    config_path = construct_path()

    # Read the workspace name from the config file


    # Create a client of Azure ML
    ml_client = MLClient.from_config(
        # Reading DefaultAzureCredential is possible when 'azd auth login' is done
        credential = DefaultAzureCredential(),
        path=config_path)

    # Verify that the handle works correctly.  
    # If you ge an error here, modify your SUBSCRIPTION, RESOURCE_GROUP, and WS_NAME in the previous cell.

    ws = ml_client.workspaces.get(read_configjson(config_path))
    print(ws.location,":", ws.resource_group)


    return ml_client



