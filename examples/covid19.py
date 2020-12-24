import pandas as pd
import sys, os

from audiorepr import audiolize

ecdc = "https://raw.githubusercontent.com/covid19-eu-zh/covid19-eu-data/master/dataset/covid-19-ecdc.csv"

df = pd.read_csv(ecdc)
df["datetime"] = pd.to_datetime(df["datetime"])
df = df.loc[df["datetime"] <= pd.to_datetime("2020-12-14T00:00:00")]
df = (
    df.pivot(index="datetime", columns="country", values="cases")
    .sort_index()[["DE", "AT", "FR"]]
    .diff()
    .dropna()
)

print(df.head())

audiolize.audiolizer(df, target="/tmp/test.midi", pitch_columns=["DE", "AT", "FR"])
