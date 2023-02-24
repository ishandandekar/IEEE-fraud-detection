from kaggle.api.kaggle_api_extended import KaggleApi
from config.core import RAW_DATA_DIR


def get_data(api: KaggleApi) -> None:
    """
    Downloads data from Kaggle

    Parameters
    ----------
    api : KaggleApi
        API credentials for Kaggle.com
    """
    api.competition_download_files("ieee-fraud-detection", RAW_DATA_DIR)


if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()
    get_data(api=api)
