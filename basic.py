from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
    return "<h1> Welcome! Go to /puppy_latin/name to see your name in puppy latin</h1>"
@app.route('/info')
def info():
    return "<h1> Puppies Information Page </h1>"

@app.route('/puppy_latin/<name>')

def puppy(name):
    if name[-1]== 'y':
        puppy_latin = name + "iful"
    else:
        puppy_latin = name + 'y'
    return "<h1> Your Puppylatin name is {}</h1>".format(puppy_latin)

if __name__ == '__main__':
    app.run()
