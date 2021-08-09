import plotly.figure_factory as f
import pandas as p
import csv

d=p.read_csv('hello.csv')

fig=f.create_distplot([d['Avg Rating'].tolist()],['RATINGS FOR DUMMIES WHO NEED A PHONE WITHOUT BUDGET CAUSE APPLE IS IN THERE TOO AND IT IS EXPENSIVE'],show_hist=False)
fig.show()