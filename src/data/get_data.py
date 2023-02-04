from kaggle.api.kaggle_api_extended import KaggleApi

def get_data(api: KaggleApi) -> None:
    """
    Downloads data from Kaggle

    Parameters
    ----------
    api : KaggleApi
        API credentials for Kaggle.com
    """
    api.competition_download_files("ieee-fraud-detection", "./data", unzip=True)
    
if __name__ == '__main__':
    api = KaggleApi()
    api.authenticate()
    get_data(api=api)