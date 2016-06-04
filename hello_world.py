from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    #return "Hello {}!".format(name.title())
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/hello/<name>/<names>")
def jedi_name(name, names):
    first = name[0:3]
    second = names[0:2]
    jedi = first + second
    html = """
        <h1>
            Your Jedi name is {}.
        </h1>
        <img src="http://eskipaper.com/images/yoda-2.jpg">
    """
    return html.format(jedi.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))