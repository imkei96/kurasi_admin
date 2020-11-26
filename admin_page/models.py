from django.urls import reverse
from neomodel import (config, StructuredNode, StringProperty, UniqueIdProperty, ArrayProperty,RelationshipTo)

class DBM(StructuredNode):
    site = StringProperty(unique_index=True, required=True)
    uid = RelationshipTo('ID', 'CHILD_ID:')

class ID(StructuredNode):
    uid = UniqueIdProperty()
    nama = RelationshipTo('Nama', 'Nama:')
    email = RelationshipTo('Email', 'Email:')
    judul = RelationshipTo('Judul', 'Judul:')
    kelas = RelationshipTo('Kelas', 'Kelas:')
    pelajaran = RelationshipTo('Pelajaran', 'Pelajaran:')
    kategori = RelationshipTo('Kategori', 'Kategori:')
    link = RelationshipTo('Link', 'Link:')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('link-uid', args=[str(self.uid)])
    def get_absolute_url_curated(self):
        return reverse('uid-curated', args=[str(self.uid)])
class Nama(StructuredNode):
    nama = StringProperty(unique_index=True)

class Email(StructuredNode):
    email = StringProperty(unique_index=True)

class Judul(StructuredNode):
    judul = StringProperty(unique_index=True)

class Kelas(StructuredNode):
    kelas = StringProperty(unique_index=True)

class Pelajaran(StructuredNode):
    pelajaran = StringProperty(unique_index=True)

class Kategori(StructuredNode):
    kategori = StringProperty(unique_index=True)

class Link(StructuredNode):
    link = ArrayProperty(unique_index=True)

# class datalog(StructuredNode):
#     uid = StringProperty
#     nama = StringProperty
#     email = StringProperty
#     judul = StringProperty
#     kelas = StringProperty
#     pelajaran = StringProperty
#     kategori = StringProperty
#     link = StringProperty
# class Log(StructuredNode):
#     logtitle = StringProperty(unique_index=True)
#     kuratorname = StringProperty()

#     connect_log = RelationshipTo()



# log = DBM(site = 'Log').save()


# kurator = ''
# kurator = 

"""
# Create Database Master
curated = DBM(site='Curated').save()
noncurated = DBM(site='NonCurated').save()
"""

"""
# Create Data ID
db = DBM.nodes.get(site='NonCurated')
data = ID().save()
db.uid.connect(data)

#Isi Data
nama = 'Hailey Stainsfield'
email = 'hshs@gmail.com'
judul = 'Membaca Cepat'
kelas = '3'
pelajaran = 'Bahasa Indonesia'
kategori = 'Membaca'
link = ['bacacepat.com', 'harusnyasihbisa.com']

#Create Child Nodes
name = Nama.get_or_create({'nama':nama})[0]
email = Email.get_or_create({'email':email})[0]
judul = Judul.get_or_create({'judul': judul})[0]
kelas = Kelas.get_or_create({'kelas': kelas})[0]
pelajaran = Pelajaran.get_or_create({'pelajaran':pelajaran})[0]
kategori = Kategori.get_or_create({'kategori':kategori})[0]
link = Link.get_or_create({'link':link})[0]

data.nama.connect(name)
data.email.connect(email)
data.judul.connect(judul)
data.kelas.connect(kelas)
data.pelajaran.connect(pelajaran)
data.kategori.connect(kategori)
data.link.connect(link)
"""
