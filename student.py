import csv
import pandas as pd
import plotly.graph_objects as go
 
v1 = pd.read_csv("data.csv")
studentnumber = v1.loc[v1['student_id'] == "TRL_987"]
print(studentnumber.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x = studentnumber.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = "h"))
fig.show()