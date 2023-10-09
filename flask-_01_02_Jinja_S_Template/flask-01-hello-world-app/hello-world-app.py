'''from flask import Flask 
app = Flask(__name__)






if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)'''

from flask import Flask
#Create an object named app from imported Flask module
app = Flask(__name__)

#Assign a URL route the hello function with decorator @app.route('/')

@app.route("/")

#Create a function hello which returns a string Hello World.
def hello():
    return "<h1>Hello World</h>"

@app.route("/second")
# Create a function second which returns a string This is the second page and assign a URL route the second function with decorator @app.route('/second')
def second():
    return "This is the second page"

#Create a dynamic url which takes id number dynamically and return with a massage which show id of page.

@app.route("/forth/<string:id>")
def forth(id):
    if id.isdigit():
        return f"The ID of this page is {id}"
    else:
        return f"{id} is not a valid ID"

app.run(debug=False)


'''

Create a function second which returns a string This is the second page and assign a URL route the second function with decorator @app.route('/second').

Create a function third which returns a string This is the subpage of third page and assign a URL route the third function with decorator @app.route('/third/subthird').

'''


