import pandas as pd

#Load Data From Excel
def ship_data_loader(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df