import pandas as pd
from loguru import logger

class FileAdapter:

    def read_csv(self, file_path, **kwargs) -> pd.DataFrame:
        logger.info(f"Reading csv from {file_path}")
        df = pd.read_csv(file_path, **kwargs)
        logger.info("Finished reading csv")
        return df