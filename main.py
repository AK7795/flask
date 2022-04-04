from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcom():
    return "welcome to my website"

@app.route("/contact")
def cont():
    return "Contacts displayed"

@app.route("/home")
def home():
    return "home page "

@app.route("/gallery")
def gall():
    return "gallery"


if __name__ == "__main__":
    app.run()
