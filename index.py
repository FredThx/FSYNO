#!/usr/bin/env python
from flask import Flask, render_template, request

from six import *
import json
import humanfriendly

app = Flask(__name__)
#url_for('static', filename='style.css')

jsonfile_name = 'ds.json'


def read_file(jsonfile_name):
    try:
        app.logger.debug("Read json file....")
        with open(jsonfile_name, 'r') as jsonfile:
            datas = json.load(jsonfile)
            app.logger.debug("ok")
    except IOError:
        app.logger.debug("No datas!")
        datas = {}
    return datas


@app.route('/')
def index():
    datas = read_file(jsonfile_name)
    sorted_id = sorted(datas.keys(), key=lambda id:datas[id]["title"])
    return render_template('index.html', datas = datas, sorted_id = sorted_id)

'''
@app.route('/total')
def total():
    datas = read_file(jsonfile_name)
    nb_tasks = len(datas)
    total_size = sum([data['size'] for data in itervalues(datas)])
    history = {}
    for data in itervalues(datas):
        for his in data['history']:
            if not his['time'] in history:
                history[his['time']]  = 0
            history[his['time']] += his['size_uploaded_dt']
    return render_template('total.html', history = history, nb_tasks = nb_tasks, total_size = total_size, humanfriendly = humanfriendly, sorted = sorted)
'''

@app.route('/task/<transfert_id>')
def datas(transfert_id):
    datas = read_file(jsonfile_name)
    return render_template('transfer.html', data = datas[transfert_id], humanfriendly = humanfriendly)


@app.route('/total',methods=['GET', 'POST'])
def total():
    if request.method == 'POST':
        period = request.form['period']
    else:
        period = 'hour'
    datas = read_file(jsonfile_name)
    nb_tasks = len(datas)
    total_size = sum([data['size'] for data in itervalues(datas)])
    tasks = sorted(datas)
    # create history : {time : {id : size, ...}, ...}
    history = {}
    for id, data in iteritems(datas):
        for his in data['history']:
            if period == 'hour':
                the_time = his['time']
            else:
                the_time = (his['time']//(24*3600))*(24*3600)
            if not the_time in history:
                history[the_time]  = {}
            if not id in history[the_time]:
                history[the_time][id] = 0
            history[the_time][id] += his['size_uploaded_dt']
    # update history : {time : [size1, size2, ...], ...}
    for the_time in history:
        new_sizes = []
        for id in tasks:
            if id in history[the_time]:
                new_sizes.append(history[the_time][id])
            else:
                new_sizes.append(0)
        history[the_time] = new_sizes
    # update tasks : [title1, title2, ...]
    tasks = [datas[task]['title'] for task in tasks]
    return render_template('total.html', history = history, nb_tasks = nb_tasks, total_size = total_size, humanfriendly = humanfriendly, sorted = sorted, tasks = tasks, period = period)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
