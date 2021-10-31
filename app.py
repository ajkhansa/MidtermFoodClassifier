from flask import Flask, render_template, request,send_from_directory, jsonify, url_for
from flask import redirect

# from scripts import helper
import requests


import json

import time
import os
import pickle

from util.read_sheet import get_sheet
from util.read_sheet import insert_row

application = Flask(__name__)

@application.route('/home')
def home():    
  return render_template('index.html')
