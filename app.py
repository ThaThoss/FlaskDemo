from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
import quandl
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure, save, output_file
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hemmelig'

class InputForm(FlaskForm):
    ticker = StringField('Ticker', validators=[DataRequired()]) 
    features = StringField('features')
    submit = SubmitField('Submit')

def get_data(form):
       quandl.ApiConfig.api_key = "8BgrwGdnNHG_Bsr5XgxR"
  
       colors=['blue','red','orange','green'] 
  
       data = quandl.get_table('WIKI/PRICES', ticker = request.form.get('ticker'),
           qopts = {'columns': ['ticker', 'date','close','adj_close','open','adj_open']},
           date = { 'gte': '2015-12-31', 'lte': '2016-12-31' },
          paginate=True)
 
       data = data.set_index('date')
      # output_file("templates/lines.html")

       p3 = figure(x_axis_type="datetime", title='Showing price for: ' + request.form.get('ticker') + ' 2016')
       c=0
       for feature in request.form.getlist('features'):
           p3.line(x=data.index,y=data[feature],legend_label=feature,line_color=colors[c])
           c=c+1
      # save(p3)
       script, div = components(p3)

        
       return script, div 



@app.route('/')
def passingon():
    return redirect(url_for('index'))

@app.route('/index', methods=["GET","POST"])
def index():
    quandl.ApiConfig.api_key = "8BgrwGdnNHG_Bsr5XgxR"
    #data = quandl.get("FRED/GDP",start_date="2020-01-01",end_date="2020-02-31")
    #db = pd.DataFrame(data)



    x = [1,2,3,4,5]
    y = [6,7,2,4,5]

    x1 = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x1]
    y1 = [10**i for i in x1]
    y2 = [10**(i**2) for i in x1]

    #output_file("templates/lines.html")

    #Create a new plot with a title and axis labels
    #p = figure(title="Simple line Example", x_axis_label="x", y_axis_label="y")

    p2 = figure(
        tools="pan,box_zoom,reset,save",
        y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
        x_axis_label="sections", y_axis_label='particles'
    ) 


    #  add a line renderer with legend and line thicness

    #p.line(x, y, legend_label="Temp.", line_width=2)

    #Add more renderers:
    p2.line(x1, x1, legend_label="y=x")
    p2.circle(x1, x1, legend_label="y=x", fill_color="white", size=8)
    p2.line(x1, y0, legend_label="y=x^2", line_width=3)
    p2.line(x1, y1, legend_label="y=10^x", line_color="red")
    p2.circle(x1, y1, legend_label="y=10^x", fill_color="red", line_color="red", size=6)
    p2.line(x1,y2, legend_label="y=10^x^2", line_color="orange", line_dash="4 4")

    form = InputForm()

    #script, div = components(p2)
    if request.method == 'POST':
        
        script, div = get_data(form)
        #return redirect(url_for('lines'))
        return render_template('plot.html', script=script, div=div)

        
        
       
            
     #   for key, value in request.form.getlist('features'):
      #      print("key: {0}, value: {1}".fomat(key, value))
        
    return render_template('index.html', form=form)



@app.route('/lines')
def lines():
    return render_template('lines.html')

@app.route('/about')
def about():
  return render_template('lines.html')
@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
  app.run(port=33507)
