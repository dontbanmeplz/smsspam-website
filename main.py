from flask import Flask, request, render_template
from imdb import IMDb
ia = IMDb()

app = Flask(__name__)
@app.route('/')
def home():
  return render_template('factors.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['MN']
    search = ia.search_movie(name) 
    for i in range(len(search)):
      id = search[i].movieID
      return search[i]['title'] + " : " + id 

if __name__ == '__main__':
  app.run(host='0.0.0.0')