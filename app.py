from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
import quandl
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
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

       p3 = figure(x_axis_type="datetime", title='Showing price for: ' + request.form.get('ticker') + ' 2016')
       c=0
       for feature in request.form.getlist('features'):
           p3.line(x=data.index,y=data[feature],legend_label=feature,line_color=colors[c])
           c=c+1
      
       script, div = components(p3)

        
       return script, div 



@app.route('/')
def passingon():
    return redirect(url_for('index'))

@app.route('/index', methods=["GET","POST"])
def index():

    form = InputForm()

    
    if request.method == 'POST':
        script, div = get_data(form)
        return render_template('plot.html', script=script, div=div)
        
    return render_template('index.html', form=form)


if __name__ == '__main__':
  app.run(port=33507)
