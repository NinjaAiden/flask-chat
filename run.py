import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomString"
messages = []

def add_messages(username, message):
    """ add messages to the 'messages' list """
    # create a timestamp based on current time
    now = datetime.now().strftime("%H:%M:%S")
    # create a dictionary to display to screen
    # passes time, user and message
    messages_dict = {"timestamp": now, "from": username, "message": message}
    # adds message to list with all necessary information
    messages.append(messages_dict)

@app.route('/', methods = ["GET", "POST"])
def index():
    """ Main page with instructions """
    if request.method == "POST":
        session["username"] = request.form["username"]
    
    if "username" in session:
        return redirect(session["username"])
    
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """
    display chat messages
    """
    return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    
@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect to chat page """
    add_messages(username, message)
    return redirect(username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)