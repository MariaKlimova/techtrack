from app import app
from flask import request, abort, jsonify, jsonrpc

PASSWORDS = {'1': '123', '2': '000', '3': 'abc'}
CHATS_LIST = ['a', 'b', 'c']
CONTACTS_LIST = ['1', '2', '3']

@app.route('/')
def dumpes():
    result = {}
    result['status_code'] = '200 OK'
    result['mimetype'] = 'application/json'
    return jsonify(result)

@app.route('/<string:name>/')
def index(name="world"):
    return "Hello, {}!".format( name )

@app.route('/form/', methods = ['GET', 'POST'])
def form():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/form/">
            <input name="first_name">
            <input name="last_name">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        rv = jsonify( request.form )
        return rv

@app.route('/chats/', methods = ['GET'])   
def chats_list():
    if request.method == "GET":
        result = {}
        result['status_code'] = '200 OK'
        result['mimetype'] = 'application/json'
        result['chats'] = CHATS_LIST
    
        return jsonify(result)

    else:
        result = {}
        result['status_code'] = '405 Method Not Allowed'
        return jsonify(result);      
 
@app.route('/contacts/', methods = ['GET'])
def contacts_list():
    if request.method == "GET":
        result = {}
        result['status_code'] = '200 OK'
        result['mimetype'] = 'application/json'
        result['contacts'] = CONTACTS_LIST

        return jsonify(result)
   
    else:
        result = {}
        result['status_code'] = '405 Method not Allowed'
        return jsonify(result);


@app.route('/new_chat/', methods = ['GET', 'POST'])
def new_chat():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/new_chat/">
            <input name ="chat_name">
            <input type="submit">
        </form>
        </body></html>"""
    else:
        result = {}
        #result['chat'] = request.form['chat_name']
        rv = jsonify( request.form)
        #CHATS_LIST.append( 
        return rv

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return """<html><head></head><body>
        <form method="POST" action="/login/">
            <input name ="login">
            <input name = password>
            <input type="submit">
        </form>
        </body></html>"""
    else:
        result = {}
        if request.form['password'] == PASSWORDS.get(request.form['login']):
            result['status_code'] = '200 OK'
            result['mimetype'] = 'application/json'
            result['final'] = 'correct'
            return jsonify(result)
        else:
            result['status_code'] = '200 OK'
            result['mimetype'] = 'application/json'
            result['final'] = 'wrong password'
            return jsonify(result)

@jsonrpc.method ('print_name')
def foo():
    return {"name": "Ivan"} 


#curl -i -X POST -H "Content-Type: application/json" --data=@request.json http://127.0.0.1
