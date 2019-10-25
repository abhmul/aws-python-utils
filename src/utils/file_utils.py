import os
import logging


def safe_open_dir(dirpath: str) -> str:
    if not os.path.isdir(dirpath):
        logging.info(f"Directory {dirpath} does not exist, creating it")
        os.makedirs(dirpath)
    return dirpath


def safe_create_file(filepath: str) -> str:
    dirpath = os.path.dirname(filepath)
    dirpath = safe_open_dir(dirpath)
    return filepath
