import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/wdbc.data")
profile = ProfileReport(df, title="Wisconsin Breast Cancer from UCI Profiling Report")
profile.to_file("report.html")


