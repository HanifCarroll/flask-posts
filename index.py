from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/hello/<name>")
def hello(name):
    return render_template('index.html', name=name.upper())


@app.route("/posts/new")
def new_post():
    return render_template('posts/new.html')


app.run()
