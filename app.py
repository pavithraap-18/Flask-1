from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return "📘 This is the About Page."

@app.route('/contact')
def contact():
    return "📞 Contact us here."
