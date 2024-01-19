import argparse
import os
from loguru import logger

from brightwheel_challenge.utils.sqlite_adapter import SqliteAdapter

class CleanJob:
    def __init__(self, target_name):
        self.target_name = target_name
        self.sql_path = os.environ.get("SQL_LOCATION")

    def run(self):
        logger.info(f"Cleaning data for {self.target_name}")

        logger.info("Loading data")
        sink_adapter = SqliteAdapter()

        query_path = os.path.join(self.sql_path, f"clean_{self.target_name}.sql")
        with open(query_path, "r") as file:
            query_string = file.read()

        drop_table = f"DROP TABLE IF EXISTS clean_{self.target_name};"
        sink_adapter.run_query(drop_table)

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS clean_{self.target_name} AS 
        {query_string}
        """

        sink_adapter.run_query(create_table_query)
        
        logger.info("Run complete")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--target-name', type=str, help='The of the final clean table')
    args = parser.parse_args()
    job = CleanJob(args.target_name)
    job.run()