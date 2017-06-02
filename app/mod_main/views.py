
from flask import Blueprint, render_template, request, redirect, url_for
mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET'])

def index():

    return render_template('login.html')