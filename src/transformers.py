import pandas as pd

#Ensure proper date format
def date_transformation(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy() #make copy to preserve original in case errors
    for col in ['Maintenance Start Date', 'Maintenance End Date', 'Docking Start Date', 'Docking End Date']:
        df2[col] = pd.to_datetime(df2[col], format='%m/%d/%y')
    return df2

#Sort by docking start date and reset index for iterrows()
def sort_duration_start(df: pd.DataFrame) -> pd.DataFrame:
    df.sort_values("Docking Start Date").reset_index(drop=True)
    return df

def add_duration(df: pd.DataFrame) -> pd.DataFrame:
    df["Maintenance Duration"] = (df["Maintenance End Date"] - df["Maintenance Start Date"]).dt.days
    df["Docking Duration"] = (df["Docking End Date"] - df["Docking Start Date"]).dt.days
    return df



