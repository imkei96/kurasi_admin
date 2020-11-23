# Python program to update 
# JSON 

import json 
from datetime import datetime
writedate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

with open('log.json') as json_file: 
	data = json.load(json_file) 
	
	temp = data['log'] 
	y = {"kurator":'Nikhil', 
        "timestamp" : writedate,
		"uid": "uidnya", 
		"action": "Accept"
		} 
	temp.append(y) 
with open('log.json','w') as f: 
    json.dump(data, f, indent=4) 
