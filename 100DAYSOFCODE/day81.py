from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates_day81')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return handle_login(request.form)
    else:
        return render_template('login.html')


def handle_login(form):
    metal = form.get('metal')
    scc = form.get('scc')
    ed209 = form.get('ed209')

    if metal == 'yes' or scc.lower() == 'yes' or ed209 == 'yes':
        return 'You are a robot'
    else:
        return 'Not a robot'


if __name__ == '__main__':
    app.run(debug=True)
