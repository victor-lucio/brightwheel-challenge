import argparse
import os
import csv
from loguru import logger

from brightwheel_challenge.utils.file_adapter import FileAdapter
from brightwheel_challenge.utils.sqlite_adapter import SqliteAdapter

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--start-date', type=str, help='The start date - format YYYY-MM-DD')
parser.add_argument('--asset-name', type=str, help='The name of the asset')
parser.add_argument('--target-name', type=str, help='The of the final raw table')

# job class
class ExtractRawJob:
    def __init__(self, start_date, asset_name, target_name):
        self.start_date = start_date
        self.asset_name = asset_name
        self.target_name = target_name
        self.file_location = os.environ.get("ASSET_LOCATION")

    def run(self):
        logger.info(f"Extracting raw data for {self.asset_name} starting on {self.start_date}")

        logger.info("Reading CSV")
        source_adapter = FileAdapter()
        df = source_adapter.read_csv(
            f"{self.file_location}{self.asset_name}.csv",
            dtype=str,
            encoding='cp1252',
            quoting=csv.QUOTE_NONE
        )
        
        logger.info("Loading data")
        sink_adapter = SqliteAdapter()

        # from the doc, data should be replaced at sink every time
        sink_adapter.load_data(df, f"raw_{self.target_name}", if_exists="replace")
        
        logger.info("Run complete")


if __name__ == "__main__":
    args = parser.parse_args()
    job = ExtractRawJob(args.start_date, args.asset_name, args.target_name)
    job.run()