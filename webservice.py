from flask import Flask
from flaskext.xmlrpc import XMLRPCHandler, Fault
app = Flask(__name__)
handler = XMLRPCHandler('api')
handler.connect(app, '/api')
@handler.register
def operator(x)):
	x= input("Enter a number to square:")
    if x == Null:
        raise Fault("please input a number")
    return x^2 
app.run()