import json
from datetime import datetime
writedate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

data = {}
data['log'] = []
data['log'].append({
    "kurator":'Nikhil', 
    "timestamp" : writedate,
	"uid": "uidnya", 
	"action": "Accept"
})

with open('log.json', 'w') as outfile:
    json.dump(data, outfile)
  