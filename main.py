import pandas as pd
import plotly.graph_objects as go

df_2021 = pd.read_csv("world-happiness-report-2021.csv")

fig = go.Figure(data=go.Choropleth(
    locations=df_2021["Country name"],
    locationmode="country names",
    z=df_2021["Ladder score"],
    text=df_2021["Country name"],
    colorscale="Earth",
    marker_line_color="white",
    marker_line_width=0.5,
    colorbar_title="Happiness Score"
))

fig.update_layout(
    title="2021 World Happiness Report",
    geo=dict(
        showframe=False,
        showcoastlines=False
    )
)

fig.show()
