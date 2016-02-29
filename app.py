from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

# config


# data


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['adduser'] == 'yes' or request.form['adduser'] == 'Yes':
            return redirect(url_for('useradd'))
        else:
            return redirect(url_for('goodbye'))
    return render_template("index.html")

@app.route('/goodbye')
def goodbye():
    return render_template("goodbye.html") 


if __name__ == '__main__':
    app.run()
