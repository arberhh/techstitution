
from flask import Blueprint, render_template, request, redirect, url_for
mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@mod_main.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
