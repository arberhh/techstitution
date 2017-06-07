
from flask import Blueprint, render_template, request, redirect, url_for
mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET'])
def index():
    arber = "Arber Haxhimusa"

    array = ['arber','diamant','festim','mendim','shpat']

    return render_template('index.html', arber_txt=arber, array=array)


@mod_main.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@mod_main.route('/<string:emri>/<string:mbiemri>', methods=['GET'])
def test(emri, mbiemri):
    array = ['arber','diamant','festim','mendim','shpat']
    if emri in array:
        emri = "%s is in array"%emri
    return render_template('test.html', emri=emri, mbiemri=mbiemri)
