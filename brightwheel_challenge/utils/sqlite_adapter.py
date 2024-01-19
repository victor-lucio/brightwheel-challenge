import pandas as pd
import os
import sqlite3
from loguru import logger

class SqliteAdapter:

    def __init__(self) -> None:
        self.database_path = os.environ.get("DATABASE_LOCATION")

    def read_dataframe(self, table_name, **kwargs) -> pd.DataFrame:
        logger.info(f"Reading data from {table_name} at {self.database_path}")
        cnx = sqlite3.connect(self.database_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx, **kwargs)
        cnx.close()
        logger.info("Finished reading data")
        return df
    
    def load_data(self, df: pd.DataFrame, table_name, **kwargs):
        logger.info(f"Loading data into {table_name} at {self.database_path}")
        cnx = sqlite3.connect(self.database_path)
        df.to_sql(table_name, cnx, **kwargs)
        cnx.close()
        logger.info("Finished loading data")

    def run_query(self, query):
        logger.info(f"Running query {query}")
        cnx = sqlite3.connect(self.database_path)
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cnx.close()
        logger.info("Finished running query")