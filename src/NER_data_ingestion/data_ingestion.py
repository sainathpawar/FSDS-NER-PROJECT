import argparse
from distutils.command.config import config
import os
# import shutil
# from tqdm import tqdm
import logging
from src.NER_utils import read_yaml, create_directories
# import random
from datasets import load_dataset


STAGE = "NER Data Preparation" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class DataIngestion:
    def __init__(self, config) -> None:
        self.config = config
        self.dataset_name = config['dataset']['name']
        self.subset = config["dataset"]["subset"]
        self.cache_dir = os.path.join(
            config["artifact"]["artifact_dir"],
            config["artifact"]["cache_dir"]
        )


    def get_data(self):
        en_data = load_dataset(self.dataset_name, self.subset, cache_dir= self.cache_dir)
        logging.info(f"dataset downloaded at:",{self.cache_dir})

def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    dataingestion = DataIngestion(config)
    dataingestion.get_data()
    

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e