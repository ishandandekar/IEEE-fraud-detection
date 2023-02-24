from pathlib import Path
import os

import yaml
from yaml.loader import SafeLoader

with open('config.yml') as stream:
    config = yaml.load(stream, Loader=yaml.loader.SafeLoader)

PACKAGE_ROOT_DIR = Path(os.getcwd()).parent.parent
DATA_DIR = PACKAGE_ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"