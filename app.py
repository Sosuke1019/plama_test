from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    """Show a list of products"""
    return 

@app.route('/register')
def register():
    """Register user"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run()