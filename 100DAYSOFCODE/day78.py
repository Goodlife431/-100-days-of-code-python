from flask import Flask

app = Flask(__name__)

myReflection = {}

myReflection["78"] = {"link": '25th october', 'Reflection': 'reflection was a bit of a head scratcher, But i got '
                                                            'there in the end'}
myReflection['79'] = {'link': '26th october', 'Reflection': 'reflection was a bit easy'}


@app.route('/<pageNumber>')
def index(pageNumber):
    global Reflections
    page = ""
    f = open("reflection.html", "r")
    page = f.read()
    f.close()

    reflection = myReflection[pageNumber]["Reflection"]
    print(reflection)
    page = page.replace("{day}", pageNumber)
    page = page.replace("{date}", myReflection[pageNumber])
    page = page.replace("{reflection}", reflection)
    return page


app.run(host='0.0.0.0', port=81)
