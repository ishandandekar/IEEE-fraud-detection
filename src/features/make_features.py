import typing as t
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from src.config.core import RAW_DATA_DIR, INTERIM_DATA_DIR, config
from src.features import feature_preprocessors

# Reading in the data
df1 = pd.read_csv(
    Path(f"{RAW_DATA_DIR}/train_transaction.csv"), usecols=config.transaction_use_cols
)
df2 = pd.read_csv(
    Path(f"{RAW_DATA_DIR}/train_identity.csv"), usecols=config.identity_use_cols
)

# merge the dataframes
dataframe = pd.merge(df1, df2, how="left", on=config.id)

# saving the merged data
dataframe.to_csv(f"{INTERIM_DATA_DIR}/dataset.csv", index=False)