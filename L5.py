#. L5 - Create Python Web Application to using Flask Web Application Framework
#importing flask module in the project is mandatary 
#an object of flask class is our WSGI application
from flask import Flask
#flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
# the route() function of the flask class is a decorator 
# while tells the application which URL should call
# the associated function.
@app.route('/')
#'/' URL is bound with hello_world()function
def hello_world():
    return 'Hello World'
# main driver function
if __name__ == '__main__':
    #run() method of flask class runs the application
    # on the local development server.
    app.run()