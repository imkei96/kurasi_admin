import datetime

from django.shortcuts import render, redirect
from django.views import generic
from neomodel import config
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .utils import change_parents, writetolog, readlog, update_database
from .models import DBM, ID, Nama, Email, Judul, Kelas, Pelajaran, Kategori, Link
from .forms import UpdateDataForm

time = datetime.datetime.now()

def get_base_context(context):
    context['time'] = time
    return context

# Create your views here.
def index(request):
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

    return render(request, 'index.html', context=context)

@login_required
def get_list(request):
    db_list = DBM.nodes.all()
    db = DBM.nodes.get(site="NonCurated")
    uid_list = db.uid.all()
    
    paginator = Paginator(uid_list, 5)
    page = request.GET.get('page')
    uid_list = paginator.get_page(page)

    context = {
        'dbm_List': db_list,
        'uid_list': uid_list,
    }
    get_base_context(context)

    # print("UID list page done:")
    # print(uid_list)    

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

@login_required
def edit_detail(request, user, uid):
    data = ID.nodes.get(uid=uid)
    nama = data.nama.all()[0]
    email = data.email.all()[0]
    judul = data.judul.all()[0]
    kelas = data.kelas.all()[0]
    pelajaran = data.pelajaran.all()[0]
    kategori = data.kategori.all()[0]
    link = data.link.all()[0]

    if request.method == 'POST':
        form = UpdateDataForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            update_database(uid,form_data)
            messages.success(request, f'Data Edited for UID {uid}!')
            action = "Edit"
            writetolog(uid, user, action)
            return redirect('index')
    else:
        form = UpdateDataForm(initial=
                              {'nama':nama.nama,
                               'email':email.email,
                               'judul':judul.judul,
                               'kelas':kelas.kelas,
                               'pelajaran':pelajaran.pelajaran,
                               'kategori':kategori.kategori,
                               'link':link.link})

    context = {
        'form':form,
        'uid':uid,
    }
    get_base_context(context)

    return render(request, 'admin_page/edit_form.html',context=context)


@login_required
def curated_list(request):
    db_list = DBM.nodes.all()
    db = DBM.nodes.get(site="Curated")
    uid_list = db.uid.all()
    # print("DB list: ")
    # print(db_list)
    # print("UID list:")
    # print(uid_list)


    paginator = Paginator(uid_list, 5)
    page = request.GET.get('page')
    uid_list = paginator.get_page(page)


    context = {
        'dbm_List': db_list,
        'uid_list': uid_list,
    }
    # print("UID list page done:")
    # print(uid_list)

    get_base_context(context)

    return render(request, 'admin_page/data_curated.html', context=context)

@login_required
def curated_detail(request, uid):
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

    return render(request, 'admin_page/UID_curated.html', context=context)

@login_required
def accept(request, user, uid):
    if request.method == 'POST':
        action = "Accept"
        writetolog(uid,user,action)
        change_parents(uid)
        messages.success(request, f'Data Accepted for UID {uid}!')
    
    return redirect('index')

@login_required
def historylog(request):

    log = readlog()
    paginator = Paginator( log, 5)
    page = request.GET.get('page')
    log = paginator.get_page(page)
    
    context = {
        'log' : log
    }
    get_base_context(context)
    # log = readlog()
    # print('log: ',context['log'])
    return render(request, 'admin_page/historylog.html',context=context)