from flask import Flask, redirect, request

app = Flask(__name__)
static_url_path = '/static'


@app.route('/home')
def home():
    return redirect("/")


@app.route('/home/portfolio')
def portfolio_second():
    return redirect("/portfolio")


@app.route('/home/linktree')
def linktree_second():
    return redirect("/linktree")


@app.route('/', methods=["GET"])
def index():
    data = request.args
    template = ""
    if data != {}:
        template = data["color"]
    page = """
    <html>
    <head>
    <link rel="stylesheet" href="static/Day76.css" />
    <title>Oduwole Oluwaseun</title>
    </head>
    <body style="background-color: {newcolor};">
    <p>Hi there!</p>
    <a href="/portfolio"
      ><button>Portfolio</button></a
    >
    <a href="/linktree"
      ><button>Link Tree</button></a
    >
    </body>
    </html>
    
    """
    page = page.replace("{newcolor}", template)

    return page


@app.route('/linktree', methods=["GET"])
def link_tree():
    data = request.args
    template = ""
    if data != {}:
        template = data["color"]
    page = """
    <html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="static/Day76.css" />
    <title>Oluwaseun's Link Tree</title>
  </head>
  <body style="background-color: {newcolor};">
    <img src="static/images/Meeee.jpg" width="auto" height="auto" />
    <h1>Oduwole Oluwaseun</h1>
    <p class="about">
      The most social and good-looking genius you'll ever meet!
    </p>
    <h3>Socials</h3>
    <ul>
      <li>
        <a href="https://twitter.com/seetax_Goodlife" target="_blank"
          ><button>Twitter (@Goodlife)</button></a
        >
      </li>
      <li>
        <a href="https://github.com/Oduwole-Oluwaseun-John" target="_blank"
          ><button>GitHub (@Goodlife)</button></a
        >
      </li>
      <li>
        <a href="http://replit.com/@Goodlife431" target="_blank"><button>Replit (@Goodlife431)</button></a>
      </li>
      <li>
        <a href="https://www.instagram.com/seetax_goodlife/" target="_blank"
          ><button>Instagram (@Goodlife)</button></a
        >
      </li>
      <li>
        <a
          href="https://www.linkedin.com/in/oduwole-oluwaseun-9b79b0258/"
          target="_blank"
          ><button>LinkedIn (Oduwole oluwaseun)</button></a
        >
      </li>
    </ul>
    <a href="/"
      ><button>Home Page</button></a
    >
    <a href="/portfolio"
      ><button>Portfolio</button></a
    >
  </body>
</html>
    """
    page = page.replace("{newcolor}", template)
    return page


@app.route('/portfolio', methods=["GET"])
def portfolio():
    data = request.args
    template = ""
    if data != {}:
        template = data["color"]
    page = """
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="static/Day76.css" />
    <title>Replit 100 Days of Code Day 73!</title>
  </head>
  <body style="background-color: {newcolor};">
    <h1>Oluwaseun's Portfolio</h1>
    <h2>Day 56 solution</h2>
    <p>
      So Day 56 was all about using csv reading and file and folder
      manipulation<br />
      to make 100 files in dozens of folders. This was tricky because the
      names<br />
      of the folders and files were based on the top 100 streaming songs and
      so<br />
      weren't simple to encode.
    </p>
    <img src="static/images/Day56image.png" />
    <a
      href="https://github.com/Oduwole-Oluwaseun-John"
      ><button>Day 56 Git Link</button>
    </a>
    <h2>Day 26 solution</h2>
    <p>
      Day 26 was about using the playsound module to play songs. I had<br />
      difficulties because I was using a newer version of the playsound
      module<br />
      but I had to downgrade to a lower version to get it to work. To figure<br />
      that out required a lot of hardwork and time of research but alas, I<br />
      solved it!
    </p>
    <img src="static/images/Day26image.png" />
    <a
      href="https://github.com/Oduwole-Oluwaseun-John"
      ><button>Day 26 Git Link</button>
    </a>
    <h2>Day 43 solution</h2>
    <p>
      Day 43 was about bingo. I was able to get a solution that was similar<br />
      to the one on the website and I felt very proud of myself.
    </p>
    <img src="static/images/Day43image.png" />
    <a
      href="https://github.com/Oduwole-Oluwaseun-John"
      ><button>Day 43 Git Link</button>
    </a>
    <h2>Day 62 solution</h2>
    <p>
      Day 62 was about using the replit DB to create a secret diary. On the<br />
      replit interface, this might have been very easy. I decided to try
      using<br />
      files to do it to challenge myself and it was difficult but it was an<br />
      amazing time coding. I felt very proud of myself for being able to<br />
      accomplish it!
    </p>
    <img src="static/images/Day62image.png" />
    <a
      href="https://github.com/Oduwole-Oluwaseun-John"
      ><button>Day 62 Git Link</button>
    </a>
    <h2>A Random Replit Day</h2>
    <p>
      This was a day when a friend of mine texted me on Twitter and told me
      that<br />
      he was also actively taking the Replit 100 Days of Code course and I
      felt<br />
      very happy to be an encouragement to someone to keep pushing and come
      out<br />
      strong!
    </p>
    <img src="static/images/RandomReplitDay.png" />
    <a href="https://twitter.com/seetax_Goodlife"
      ><button>My Twitter Link</button></a
    >
    <a href="/"
      ><button>Home</button></a
    >
    <a href="/linktree"
      ><button>Link Tree</button></a
    >
  </body>
</html>
    """

    page = page.replace("{newcolor}", template)
    return page


app.run(host='0.0.0.0', port=5000)