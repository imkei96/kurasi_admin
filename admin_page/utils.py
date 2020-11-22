from neomodel import db, config
from .models import DBM, ID, Nama, Email, Judul, Kelas, Pelajaran, Kategori, Link

config.DATABASE_URL = 'bolt://neo4j:admin@localhost:7687'


def filter_nodes(node_type, search_text):
    node_set = node_type.nodes

    if node_type.__name__ == 'ID':
        node_set.filter(UID__icontain=search_text)

    return node_set

def fetch_UIDs_NonCurated():
    nodelist = []
    nodes = db.cypher_query(
        '''
        MATCH (n:DBM {site: 'NonCurated'})-[]->(id)
        RETURN id.uid
        '''
    )
    nodes = nodes[0]
    for x in nodes:
        nodelist.append(x[0])
    return nodelist

def fetch_UID_Childs(uid_name):
    data = {}
    nodes = ID.nodes.get(uid=uid_name)
    data['nama'] = nodes.nama.all()
    data['email'] = nodes.email.all()
    return data
def change_parents(idunik):
    
    dbnc = DBM.nodes.get(site="NonCurated")
    dbc = DBM.nodes.get(site="Curated")
    list_nc = dbnc.uid.all()
    list_c = dbc.uid.all()
    
    for x in list_nc:
        if x.uid == idunik:
            dbnc.uid.disconnect(x)
    for x in ID.nodes:
        if x.uid == idunik:
            print(x)
            dbc.uid.connect(x)    
    
# change_parents('7b6372d9f3ac407f96d872dc1350eeca')

def fetch_NonCurated():
    nodelist = []
    nodes = db.cypher_query(
        '''
        MATCH (n:DBM {site: 'NonCurated'})-[]->(id)
        RETURN id
        '''
    )
    nodes = nodes[0]
    for x in nodes:
        nodelist.append(x[0])
    return nodelist
def fetch_curated():
    dbc = DBM.nodes.get(site="Curated")
    list_c = dbc.uid.all()    
    print("list curatd")
    for y in list_c:
        print(y)    

# for x in fetch_NonCurated():
#     print(x)
