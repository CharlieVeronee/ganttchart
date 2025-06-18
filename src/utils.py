import pandas as pd

def summary_stats(df: pd.DataFrame)-> pd.DataFrame:
    stats = df[["Maintenance Duration", "Docking Duration"]].agg(["count", "mean", "median", "min", "max"]).transpose()
    #agg applies functions to each column, transpose swaps rows and columns
    stats = stats.rename(
    index={
            "Maintenance Duration": "Maintenance",
            "Docking Duration": "Docking"
        }
    )
    stats["mean"]   = stats["mean"].round(1)
    stats["median"] = stats["median"].astype(int)
    stats["min"]    = stats["min"].astype(int)
    stats["max"]    = stats["max"].astype(int)
    
    return stats
