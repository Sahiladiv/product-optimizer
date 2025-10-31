from flask import Blueprint, render_template, jsonify
import json

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def homepage():
    with open('data/scrapped_data.json') as f:
        data = json.load(f)
    return render_template('home.html', product=data)


# get data from json -> make a macrosite -> crawl that -> use AI agents over that