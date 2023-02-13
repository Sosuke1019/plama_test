from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/other')
def other():
    return 

if __name__ == "__main__":
    app.run()