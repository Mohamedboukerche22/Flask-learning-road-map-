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
