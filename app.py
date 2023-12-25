from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "World"
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
