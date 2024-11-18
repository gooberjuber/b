from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO


# JSON-like configuration dictionary
config = {
    "azure_blob": {
        "connection_string": "",
        "container_name": "databricks-storage-container"
    }
}

# Extract connection string and container name from the config dictionary
connection_string = config["azure_blob"]["connection_string"]
container_name = config["azure_blob"]["container_name"]

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Function to upload CSV data to Azure Blob Storage
def upload_csv_to_blob(blob_name, dataframe):
    try:
        # Convert DataFrame to CSV format
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload CSV to blob
        blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
        return {
            "success" : True,
            "data" : None,
            "error" : None
        }

    except Exception as e:
        return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }

# Function to read CSV data from Azure Blob Storage
def read_csv_from_blob(blob_name):
    try:
        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Download the blob data as a string
        blob_data = blob_client.download_blob().readall()

        # Load the CSV data into a DataFrame
        csv_data = pd.read_csv(StringIO(blob_data.decode("utf-8")))

        return {
            "success" : True,
            "data" : csv_data,
            "error" : None
        }


    except Exception as e:
       return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }
