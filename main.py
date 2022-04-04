from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcom():
    return "welcome to my website"


@app.route("/contact")
def cont():
    return render_template("contact.html")


@app.route("/home")
def home():
    return "home page "


@app.route("/gallery")
def gall():
    return "add ur pics here"


if __name__ == "__main__":
    app.run()
