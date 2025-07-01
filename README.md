# Flask-learning-road-map-
# 1 - installing flask 
*ubuntu and debian*
```bash
sudo apt install python3 pip3
python -m venv venv #creat python env
source venv/bin/activate
```
*fedora*
```bash
sudo dnf install python3 pip3
python -m venv venv
source venv/bin/activate
```
*there is no arch lol*

```bash
pip install Flask
```
# 2-how to code it 

*in python use*

`from flask import Flask`

and try to code like `first.py`

# using template html file
to call it use `from flask import render_template`

to use it you can just use 

```py
@app.route('/')
def home():
 render_template('home.html')
```

# 'GET' - 'POST'
we use 
*GET*
`request.args.get('query', 'لا يوجد')` to find some data 
*POST*
`name = request.form['name']` to send some data 

we should use on the html file 
```html
<form method="POST">
   <input name = "name">
   <input type = "submit">
</form>
```
all in one code 
```py
from flask import Flask ,request ,render_template

app = Flask(__name__)

@app.route('/form' , mothods=['GET','POST'])
def form():
  if request.mothod == 'POST':
    username = request.form['username']
    return f"hello {username} to flask app "
  else :
    name = request.args.get('username',"no one ")
    return f"hello {username} from get"

if __name__ == __main__:
   app.run(debug = True)
```
usefull trick on register websites using flask

```html
{% if error %}
  <p style="color:red">{{ error }}</p>
{% endif %}
```
