from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_excel("verlegenhuken.xlsx")
x=df["Temperature"]/10
y=df["Pressure"]/10

output_file("Line.html")

f=figure(plot_width=500,plot_height=400, tools='pan',logo=None)

f.title.text="Temperature Pressure Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color="Blue"
f.yaxis.minor_tick_line_color="Red"
f.xaxis.axis_label="Temperature"
f.yaxis.axis_label="Pressure"

f.circle(x,y,size=0.5)

show(f)
