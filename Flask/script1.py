#git hidden folder
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, output_file, show
    from bokeh.embed import components
    from bokeh.resources import CDN

    start_t=datetime.datetime(2018,8,25)
    end_t=datetime.datetime(2018,10,25)

    df= data.DataReader(name="AAPL", data_source="yahoo",start= start_t, end = end_t)

    i=0

    '''Status column is added and the values are assigned'''

    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c < o:
            value="Decrease"
        else:
            value="Equal"
        return value

    df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df["Middle"]= (df.Open + df.Close)/2
    df["Height"]= abs(df.Open - df.Close)

    f= figure(x_axis_type ='datetime', width=1000, height=400, sizing_mode="scale_width")
    f.title.text="Candle Stick Graph"
    '''line represents high and low and bar represnt open AND CLOSE '''

    hours_12=12*60*60*1000
    f.segment(df.index, df.High, df.index, df.Low, line_color="Black")
    '''segment before rectangles on chart: overlapping issue; parameters are x and y coordinate of 2 end points'''

    f.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color="#CCFFFF",line_color="Black")
    f.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color="#FF3322",line_color="Black")

    f.grid.grid_line_alpha= 0.3 #opacity

    '''extract script and div components'''
    script1, div1= components(f)
    cdn_js_link= CDN.js_files
    cdn_css_link= CDN.css_files

    #output_file=("Chart.html")
    #show(f)
    #print(df)
    print("Plot")
    df.to_csv("E:/PYTHON/UDEMY PROJECTS/Stock Market Analysis/Flask/Data.csv")

    '''pass the parameters'''
    return render_template("plot.html", script1=script1 , div1 =div1, cdn_js_link=cdn_js_link, cdn_css_link= cdn_css_link)

@app.route('/')
def home():
    #return "This is a home page!"

    print ("Home")
    return render_template("home.html")

@app.route('/about/')
def about():
    #return "This is about page!"
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
