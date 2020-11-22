import datetime

from django.shortcuts import render
from django.views import generic
from neomodel import config
from django.contrib.auth.decorators import login_required

from .models import DBM, ID, Nama, Email, Judul, Kelas, Pelajaran, Kategori, Link

config.DATABASE_URL = 'bolt://neo4j:admin@localhost:7687'
time = datetime.datetime.now()

def get_base_context(context):
    context['time'] = time
    return context

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_data = len(DBM.nodes.all())
    num_uid = len(ID.nodes.all())
    num_nama = len(Nama.nodes.all())
    num_email = len(Email.nodes.all())
    num_judul = len(Judul.nodes.all())
    num_kelas = len(Kelas.nodes.all())
    num_pelajaran = len(Pelajaran.nodes.all())
    num_kategori = len(Kategori.nodes.all())
    num_link = len(Link.nodes.all())

    context = {
        'num_data': num_data,
        'num_uid': num_uid,
        'num_nama': num_nama,
        'num_email': num_email,
        'num_judul': num_judul,
        'num_kelas': num_kelas,
        'num_pelajaran': num_pelajaran,
        'num_kategori': num_kategori,
        'num_link': num_link
    }
    get_base_context(context)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@login_required
def get_list(request):
    db_list = DBM.nodes.all()
    db = DBM.nodes.get(site="NonCurated")
    uid_list = db.uid.all()

    context = {
        'dbm_List': db_list,
        'uid_list': uid_list,
    }
    get_base_context(context)
    return render(request, 'admin_page/data.html', context=context)

@login_required
def get_detail(request, uid):
    data = ID.nodes.get(uid=uid)
    nama = data.nama.all()
    email = data.email.all()
    judul = data.judul.all()
    kelas = data.kelas.all()
    pelajaran = data.pelajaran.all()
    kategori = data.kategori.all()
    link = data.link.all()
    context = {
        'uid': uid,
        'nama': nama,
        'email': email,
        'judul': judul,
        'kelas': kelas,
        'pelajaran': pelajaran,
        'kategori': kategori,
        'link': link,
    }
    get_base_context(context)

    return render(request, 'admin_page/UID.html', context=context)
