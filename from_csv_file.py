from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#df=pandas.read_csv("data.csv")
#x=df["x"]
#y=df["y"]

df=pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
x=df["Year"]
y=df["Engineering"]

output_file("Line.html")

f=figure()
f.line(x,y)
show(f)
