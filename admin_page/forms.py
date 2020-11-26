from django import forms

class UpdateDataForm(forms.Form):
    nama = forms.CharField()
    email = forms.EmailField()
    judul = forms.CharField()
    kelas = forms.CharField()
    pelajaran = forms.CharField()
    kategori = forms.CharField()
    link = forms.CharField()