
from flask import Blueprint, render_template, request, redirect, url_for,Response
from app import mongo
from bson import ObjectId
import json
mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET','POST'])
def index():
    db = mongo.db.reports
    if request.method == 'GET':
        reports = db.find()
        return render_template('index.html', reports=reports)
    elif request.method == 'POST' :
        print request.form
        mongo.db.reports.insert({
            "name": request.form['name'],
            "last_name":request.form['last_name']
        })
        return redirect(url_for('main.index'))

@mod_main.route('/add-people', methods=['GET', 'POST'])
def add_people():
    #TODO Implement POST REQUEST
    # if fail:
        # build logic
    # if success:
        # build logic
    return "JSON RESULT"

@mod_main.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
'''@mod_main.route('/remove/<string:id>', methods=['GET'])
def remove(id):
    if request.method == 'GET':
    db = mongo.db.reports
    db = db.remove({"_id":ObjectId(id)})
    return redirect(url_for('main.index'))'''

@mod_main.route('/remove/<string:report_id>', methods=['GET'])
def remove(report_id):
    if request.method == 'GET':
        mongo.db.reports.remove({"_id": ObjectId(report_id)})
        return Response(json.dumps({"removed": True}), mimetype='application/json')

@mod_main.route('/remove', methods=['POST'])
def remove_report():
    if request.method == 'POST':
        report_id = request.form['report_id']
        mongo.db.reports.remove({"_id": ObjectId(report_id)})
        return Response(json.dumps({"removed": True}), mimetype='application/json')

@mod_main.route('/audit', methods=['GET','POST'])
def audit():
    db = mongo.db.reports
    if request.method == 'GET':
        reports = db.find()
        return render_template('audit.html')
    elif request.method == 'POST':
        print request.form
        mongo.db.reports.insert(request.form.to_dict())
        return redirect(url_for('main.audit'))
@mod_main.route('/newNc', methods=['GET','POST'])
def newNc():
    db = mongo.db.reports
    if request.method == 'GET':
        reports = db.find()
        return render_template('newNc.html')
    elif request.method == 'POST':
        print request.form
        mongo.db.reports.insert(request.form.to_json())
        return redirect(url_for('main.newNc'))
@mod_main.route('/documentR',methods=['GET','POST'])
def documentR():
        db = mongo.db.reports
        if request.method == 'GET':
            reports = db.find()
            return render_template('documentR.html')
        elif request.method == 'POST':
            print request.form
            mongo.db.reports.insert(request.form.to_json())
            return redirect(url_for('main.documentR'))
