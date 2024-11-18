import pandas as pd
import logging
import azure_services

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_df(blob_name : str):
    try:
        
        df_read = azure_services.read_csv_from_blob(blob_name)
        
        if df_read['success'] == True:
            df_read = df_read['data']
        else:
            return {
            "success" : False,
            "data" : None,
            "error" : df_read['error']
            }

        return {
            "success" : True,
            "data" : df_read,
            "error" : None
        }
    
    except Exception as e:
        logger.error(f"load_def fn {str(e)}")
        return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }


def get_rows_df(df : pd.DataFrame, column1_name : str, column2_name : str) -> list[dict]:
    try:

        rows = []

        for index, row in df.iterrows():
            rows.append({"row" : index, column1_name : row[column1_name], column2_name : row[column2_name]})

        return {
            "success" : True,
            "data" : rows,
            "error" : None
        }
    
    except Exception as e:
        logger.error(f"get_rows_df {str(e)}")
        return {
            "success" : False,
            "data" : None,
            "error" : str(e)
        }
