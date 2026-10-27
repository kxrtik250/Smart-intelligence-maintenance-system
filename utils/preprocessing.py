import pandas as pd

def clean_sensor_df(df: pd.DataFrame):
    df = df.copy()
    df = df.select_dtypes(include=['number'])
    df = df.ffill().bfill()
    return df
