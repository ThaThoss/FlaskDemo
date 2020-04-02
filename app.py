from flask import Flask, render_template, request, redirect
import quandl

quandl.ApiConfig.api_key = "8BgrwGdnNHG_Bsr5XgxR"

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')
@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
  app.run(port=33507)
