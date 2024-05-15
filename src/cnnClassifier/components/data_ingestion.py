import os
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                self.config.source_URL,
                self.config.local_data_file
            )
            logger.info(f"Downloaded {get_size(Path(self.config.local_data_file))} from {self.config.source_URL} to {self.config.local_data_file}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists")
            logger.info(f"File size: {get_size(Path(self.config.local_data_file))}")
    
    def unzip_data(self):
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)
            logger.info(f"Created directory {self.config.unzip_dir}")
        else:
            logger.info(f"Directory {self.config.unzip_dir} already exists")
        
        logger.info(f"Unzipping {self.config.local_data_file} to {self.config.unzip_dir}")
        import zipfile
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Unzipped {self.config.local_data_file} to {self.config.unzip_dir}")

