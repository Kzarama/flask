from flask import Flask, request, make_response, redirect

# name flask app
app = Flask(__name__)
# debug mode
app.run(debug=True)

# decorator with the path


@app.route('/')
# method of the route
def index():
    # user address
    user_ip = request.remote_addr
    # redirect to the path /hello
    response = make_response(redirect('hello'))
    # set cookie with the user address
    response.set_cookie('user_ip', user_ip)
    # return the response
    return response

# decorator with the path


@app.route('/hello')
# method of the route
def hello():
    # get the cookie with the user address
    user_ip = request.cookies.get('user_ip')
    # return the message
    return f'Hello world flask {user_ip}'
