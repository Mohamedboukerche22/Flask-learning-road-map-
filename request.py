from flask import Flask,request

app = Flask(__name__)

@app.route('/greet', methods = ['GET' , 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}"
    return '''
    <form method = 'POST'>
    <input name = "name">
    <input type ="submit">
    </form>
    '''

if __name__ =='__main__':
    app.run(debug = True)
