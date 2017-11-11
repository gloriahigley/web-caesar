from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0"/><br>
        <textarea name="text"></textarea><br>
        <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt(): 
    rot = request.form['rot']
    text = request.form['text']
    text2 = rotate_string(text, int(rot))
    return '<h1>Hello, ' + text2 + '</h1>'
app.run()