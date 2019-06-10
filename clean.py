import json
try:
    jsonfile_name = sys.argv[1]
except:
    jsonfile_name = 'ds.json'
try:
    with open(jsonfile_name, 'r') as jsonfile:
        datas = json.load(jsonfile)
except IOError:
    datas = {}


for id in datas:
    if 'history' in datas[id]:
        datas[id]['history'] = [h for h in datas[id]['history'] if h['size_uploaded_dt'] > 0 and 'time' in h]
        for h in datas[id]['history']:
            h['time'] = int(h['time'])
            h['dt'] = int(h['dt'])

#Save file
with open(jsonfile_name,'w') as jsonfile:
    json.dump(datas, jsonfile, indent = 4)
