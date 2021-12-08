# Import dependencies
from flask import Flask

# Create new flask instance called app
app = Flask(__name__)

# Create flask route
@app.route('/')
def hello_world():
    return 'Hello world'
