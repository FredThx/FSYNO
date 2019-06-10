from synopy.base import Connection
#from synopy.api import DownloadStationInfo
from synopy.api import DownloadStationTask

import json
import time
import sys

try:
    jsonfile_name = sys.argv[1]
except:
    jsonfile_name = 'ds.json'

try:
    with open(jsonfile_name, 'r') as jsonfile:
        datas = json.load(jsonfile)
except IOError:
    datas = {}

conn = Connection('http','192.168.10.10', port = 5000)
conn.authenticate('admin', 'GaZoBu')

dstask_api = DownloadStationTask(conn, version=1)
tasks = dstask_api.list(additional='transfer').payload[u'data'][u'tasks']

now = int(time.time())

#Update datas and calculate size size_uploaded during dt
for task in tasks:
    id = task[u'id']
    if not id in datas:
        datas[id]={}
        datas[id]['now'] = now
        datas[id]['history'] = []
    else:
        size_uploaded_dt = task['additional']['transfer']['size_uploaded'] - datas[id]['additional']['transfer']['size_uploaded']
        if size_uploaded_dt>0:
            datas[id]['history'].append({
                        'time' : now,
                        'dt' : now - datas[id]['now'],
                        'size_uploaded_dt' : size_uploaded_dt
                        })
        datas[id]['now'] = now
    datas[id].update(task)

#Remove old task from datas
ids = [task['id'] for task in tasks]
for id in [id for id in iter(datas) if not id in ids]:
    del datas[id]

#Save file
with open(jsonfile_name,'w') as jsonfile:
    json.dump(datas, jsonfile, indent = 4)
