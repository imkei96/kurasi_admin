from neomodel import db, config
from .models import DBM, ID, Nama, Email, Judul, Kelas, Pelajaran, Kategori, Link

from datetime import datetime
import json


def get_value(data,cls):
    if cls == 'Nama':
        return data.nama
    if cls == 'Email':
        return data.email
    if cls == 'Judul':
        return data.judul
    if cls == 'Kelas':
        return data.kelas
    if cls == 'Pelajaran':
        return data.pelajaran
    if cls == 'Kategori':
        return data.kategori
    if cls == 'Link':
        return data.link

def change_data(uid,data,new_data,cls):
    parent_node = ID.nodes.get(uid=uid)
    old_node = data
    if cls == 'Nama':
        new_node = Nama.get_or_create({'nama':new_data})[0]
        parent_node.nama.connect(new_node)
        parent_node.nama.disconnect(old_node)
    if cls == 'Email':
        new_node = Email.get_or_create({'email':new_data})[0]
        parent_node.email.connect(new_node)
        parent_node.email.disconnect(old_node)
    if cls == 'Judul':
        new_node = Judul.get_or_create({'judul':new_data})[0]
        parent_node.judul.connect(new_node)
        parent_node.judul.disconnect(old_node)
    if cls == 'Kelas':
        new_node = Kelas.get_or_create({'kelas':new_data})[0]
        parent_node.kelas.connect(new_node)
        parent_node.kelas.disconnect(old_node)
    if cls == 'Pelajaran':
        new_node = Pelajaran.get_or_create({'pelajaran':new_data})[0]
        parent_node.pelajaran.connect(new_node)
        parent_node.pelajaran.disconnect(old_node)
    if cls == 'Kategori':
        new_node = Kategori.get_or_create({'kategori':new_data})[0]
        parent_node.kategori.connect(new_node)
        parent_node.kategori.disconnect(old_node)
    if cls == 'Link':
        new_node = Link.get_or_create({'link':new_data})[0]
        parent_node.link.connect(new_node)
        parent_node.link.disconnect(old_node)

    query = "MATCH (b) WHERE NOT exists(()-[]->(b)) AND NOT (b:DBM) DELETE (b)"
    results, meta = db.cypher_query(query)
    return 0

def update_database(uid,form_data):
    class_list_txt = ['Nama','Email','Judul','Kelas','Pelajaran','Kategori','Link']
    class_list = [Nama,Email,Judul,Kelas,Pelajaran,Kategori,Link]
    class_properties = ['nama','email','judul','kelas','pelajaran','kategori','link']

    for cls in class_list_txt:
        query = "MATCH (a:ID)-[]->(b:"+cls+") WHERE a.uid CONTAINS'"+uid+"' RETURN (b)"
        results, meta = db.cypher_query(query)
        class_type = class_list[class_list_txt.index(cls)]
        data = class_type.inflate(results[0][0])

        old_data = get_value(data, cls)
        new_data = form_data[class_properties[class_list_txt.index(cls)]]

        if cls == 'Link':
            new_list = []
            for x in list(new_data[1:-1].split(",")):
                new_list.append(x.strip()[1:-1])
            new_data = list(new_list)

        if old_data != new_data:
            change_data(uid, data, new_data, cls)


    # If old data == new data
    # No change

    # If old data != new data
    # 1. get_or_create new data, connect to uid
    # 2. disconnect old data
    # 3. delete all old data with no UID parents

def change_parents(idunik):
    dbnc = DBM.nodes.get(site="NonCurated")
    dbc = DBM.nodes.get(site="Curated")

    list_nc = dbnc.uid.all()
    list_c = dbc.uid.all()

    node = ID.nodes.get(uid=idunik)

    dbnc.uid.disconnect(node)
    dbc.uid.connect(node)

# change_parents('7b6372d9f3ac407f96d872dc1350eeca')
def writetolog(uid,kurator,action):
    writedate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    with open('./admin_page/log.json') as json_file: 
        data = json.load(json_file) 
        
        temp = data['log'] 
        y = {"kurator":kurator, 
            "timestamp" : writedate,
            "uid": uid, 
            "action": action,
            } 
        temp.append(y) 
    with open('./admin_page/log.json','w') as f: 
        json.dump(data, f, indent=4) 
    
def readlog():
    with open('./admin_page/log.json') as json_file:
        data = json.load(json_file)
        # for p in data['log']:
        #     print('kurator: ' + p['kurator'])
        #     print('timestamp: ' + p['timestamp'])
        #     print('uid: ' + p['uid'])
        #     print('action: ' + p['action'])
        #     print('') 
    return data['log']
# print(readlog())

