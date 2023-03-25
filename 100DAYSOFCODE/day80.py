from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates_day80')

VALID_CREDENTIALS = {'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3'}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
            return redirect(url_for('nice', username=username))
        else:
            return redirect(url_for('naughty'))
    else:
        return render_template('login.html')


@app.route('/nice/<username>')
def nice(username):
    return render_template('nice.html', username=username)


@app.route('/naughty')
def naughty():
    return render_template('naughty.html')


if __name__ == '__main__':
    app.run(debug=True)
