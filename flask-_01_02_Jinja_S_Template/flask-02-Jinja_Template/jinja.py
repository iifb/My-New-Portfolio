'''from flask import Flask, render_template

app = Flask(__name__)








if __name__== "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)'''

from flask import Flask, render_template

#Create an object named app from imported Flask module.

app = Flask(__name__)

#Create a function named head which sends number number1 and number2 variables to the index.html. 
# #Use these variables into the index.html file. Assign a URL route the head function with decorator @app.route('/').

@app.route("/")

def head():
    return render_template("index.html", number1=10, number2=20)

@app.route("/entries/<string:num1>/<string:num2>")

def custom(num1,num2):
    if num1.isdigit() and num2.isdigit():

        return render_template("index.html", number1=num1, number2=num2)
    else:
        return f"{num1} and {num2} must be numbers only"
    
@app.route("/sum/<string:a>/<string:b>")

def customadd(a,b):
    if a.isdigit() and b.isdigit():
        total = int(a) + int(b)
        
        html_code = render_template("body.html", value1=a, value2=b, sum=total)
        return html_code
    else:
        return f"{a} and {b} must be numbers only"


app.run(debug=False)

#Create an body.html file under templates folder.

#Create a function named number which sends number num1 and num2 and sum of them to the index.html. Use these variables into the body.html file. 
# #Assign a URL route the number function with decorator @app.route('/sum').

