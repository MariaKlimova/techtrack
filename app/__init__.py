from flask import Flask

from flask_jsonrpc import JSONRPC
app = Flask(__name__)

from .views import *
