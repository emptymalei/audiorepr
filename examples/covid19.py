import pandas as pd
from audiorepr import audiolize

ecdc = "https://gist.githubusercontent.com/emptymalei/90869e811b4aa118a7d28a5944587a64/raw/1534670c8a3859ab3a6ae8e9ead6795248a3e664/ecdc%2520covid%252019%2520data"

df = pd.read_csv(ecdc, index_col="datetime")
df = df.loc[pd.to_datetime(df.index) >= pd.to_datetime("2020-08-01")]

audiolize.audiolizer(df, target="/tmp/test.midi", pitch_columns=["DE", "FR"])
