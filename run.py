import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "some_secret"

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            port=int(os.environ.get("5000")),
            debug=False)
            
