import pandas as pd

import plotly.express as px

df = pd.read_csv("C:\Users\hitesh\Desktop\Whitehat.Jr\Capstone Class 102\Data-visualization-master\csv files\line_chart.csv")

fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

fig.show()
