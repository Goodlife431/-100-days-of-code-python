from flask import Flask
import datetime
from flask import Flask, send_file

app = Flask(__name__, static_url_path="/static")
today = datetime.date.today()

app = Flask(__name__)


@app.route('/image')
def image():
    filename = 'static/images/seun.jpg'
    return send_file(filename, mimetype='image/jpg')


@app.route('/')
def index():
    page = f"""
    {today}
    <html>
    <body>
    <p><a href = "/home"> Go home </a></p>
    </body>
    </html>
    """
    return page


@app.route('/home')
def home():
    page = f"""
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
</head>
<body>
<h2> {today}</h2>
<img src="{{ url_for('image') }}" alt="images">
  <h1>Oduwole Oluwaseun</h1>
  <p class="about">
    The richest man in the world
  </p>
  <h3>Socials</h3>
  <ul>
    <li>Twitter: @seetax_Goodlife</li>
     <li>YouTube: Oduwole Oluwaseun</li>
     <li>replit: @Goodlife431</li>
  </ul>
</body>

</html>

  """
    return page


app.run(host='0.0.0.0', port=81)


@app.route('/linktree')
def linktree():
    page = f"""
  <html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
</head>
<body>
<h2> {today}</h2>
<img src="{{ url_for('image') }}" alt="images">
  <h1>Oduwole Oluwaseun</h1>
  <p class="about">
    The richest man in the world
  </p>
  <h3>Socials</h3>
  <ul>
    <li>Twitter: @seetax_Goodlife</li>
     <li>YouTube: Oduwole Oluwaseun</li>
     <li>replit: @Goodlife431</li>
  </ul>
</body>

</html>

  """
    return page
