from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("adbe.csv", parse_dates=["Date"])
x=df["Date"]
y=df["Close"]

output_file("Timeseries.html")

f=figure(plot_width=500,plot_height=250, x_axis_type="datetime", sizing_mode='scale_width')

f.title.text="Temperature Pressure Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color="Blue"
f.yaxis.minor_tick_line_color="Red"
f.xaxis.axis_label="DateClose"
f.yaxis.axis_label="Pressure"

f.line(x,y,color="Blue",alpha=0.5)

show(f)
