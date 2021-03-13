from flask import Flask

app = Flask(__name__)

@app.route("/")

def head():
    return "HELLO_ WeORLD"    
@app.route("/firstpage")
def first ():
    return "this is first page"


@app.route("/secondpage")
def second():
    return "this is second page too"

@app.route("/thirdpage")

def third(id=5):
    
    return f'this is {id} page too'

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'
if __name__ == '__main__':
    app.run(debug = True)
