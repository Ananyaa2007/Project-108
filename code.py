import random 
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd 

df = pd.read_csv("data.csv")
fig1 = ff.create_distplot([df["Avg Rating"].tolist()],["Average Rating for Mobile Brands"])
fig1.show()