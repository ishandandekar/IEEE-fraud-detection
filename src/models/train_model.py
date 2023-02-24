import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from src.config.core import INTERIM_DATA_DIR, config
from src.features import feature_preprocessors

dataset = pd.read_csv(f"{INTERIM_DATA_DIR}/dataset.csv")

X = dataset[config.all_features]
y = dataset[config.target]

# Pipeline for feature transformation
fraud_detection_pipe = Pipeline(
    [
        (
            "most_frequent_imputer",
            feature_preprocessors.MostFrequentImputer(
                features=config.impute_most_freq_cols
            ),
        ),
        (
            "aggregate_high_cardinality_features",
            feature_preprocessors.AggregateCategorical(
                features=config.high_cardinality_cats
            ),
        ),
        (
            "get_categorical_codes",
            feature_preprocessors.CategoryConverter(
                features=config.convert_to_category_codes
            ),
        ),
        (
            "mean_imputer",
            feature_preprocessors.MeanImputer(features=config.continuous_features),
        ),
        (
            "random_forest_clf",
            RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42),
        ),
    ]
)

fraud_detection_pipe.fit(X, y)

# Saving the model pipeline
joblib.dump(fraud_detection_pipe, "pipeline.pkl")
