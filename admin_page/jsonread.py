import json

with open('log.json') as json_file:
    data = json.load(json_file)
    for p in data['log']:
        print('kurator: ' + p['kurator'])
        print('timestamp: ' + p['timestamp'])
        print('uid: ' + p['uid'])
        print('action: ' + p['action'])
        print('')
