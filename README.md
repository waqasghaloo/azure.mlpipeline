# azure.mlpipeline

[Tutorial](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-azure-ml-in-a-day?view=azureml-api-2#create-training-script)

[There are two CLIs provided by Azure 'az' and 'azd'](https://devblogs.microsoft.com/azure-sdk/introducing-the-azure-developer-cli-a-faster-way-to-build-apps-for-the-cloud/)
##### The Azure Developer CLI (azd) is intended to be complementary to the Azure CLI (az). With the Azure Developer CLI, we keep the commands you use high-level and mapped to stages your development workflow. By keeping things high-level some of the nitty gritty control plane management pieces get abstracted away so that you can focus on writing code. If you want to do more fine-tuned management of Azure resources, your best bet is the Azure CLI. With azd, you get prebuilt templates and focus on writing code rather than building completing application from scratch.

[Learning Series Youtube](https://www.youtube.com/playlist?list=PLlrxD0HtieHjDop2DtiCmwTTcrlwKAVHE)

#### Authenticate
[Install Azure CLI Developer azd on VSCode](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows)
##### Authenticate using 'azd auth login' and credentials will be brought to DefaultCredentials class

[Installation of az CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)

#### Setup Environment
[Setup development environment of Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment?view=azureml-api-2#local-and-dsvm-only-create-a-workspace-configuration-file)

### Step #1: Create an Azure ML client/handle

[Connect with created workspace](https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.mlclient?view=azure-python#azure-ai-ml-mlclient-from-config)

[Store configurations in config.json file](https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.mlclient?view=azure-python#azure-ai-ml-mlclient-from-config)
