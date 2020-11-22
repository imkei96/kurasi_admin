from neomodel import db, config
#from .models import ID, Nama, Email, Judul, Kelas, Kategori, Link

config.DATABASE_URL = 'bolt://admin:admin@localhost:7687'

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
