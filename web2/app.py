from flask import Flask , request ,render_template
app = Flask(__name__)
@app.route('/' , methods =['POST','GET'])
def login():
  if request.method =='POST':
     username = request.form['username']
     return f"hello {username} welcome back! "
  return render_template('register.html' , username = 'username')



if __name__ =='__main__':
    app.run(debug = True)    
