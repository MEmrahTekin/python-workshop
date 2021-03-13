from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def head ():
    return render_template("index.html", number = 15, number2=40)

@app.route("/carp")
def number():
    number1 , number2 = 20 ,30
    return render_template("body.html", num1=number1, num2=number2, multipy= number1* number2)
     
if __name__ == "__main__":
    app.run(debug= True)