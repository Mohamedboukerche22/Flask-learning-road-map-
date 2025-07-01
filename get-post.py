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
