import pandas as pd
import sys, os

from audiorepr import audiolize

de = "https://raw.githubusercontent.com/covid19-eu-zh/covid19-eu-data/master/dataset/covid-19-de.csv"

df = pd.read_csv(de)

print(df.head())

audiolize.audiolizer(df, target="/tmp/test.midi", pitch_columns=["cases"])
