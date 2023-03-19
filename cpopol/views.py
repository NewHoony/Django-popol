from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Port
# Create your views here.

class PortListView(ListView):
    model = Port
    template_name = 'cpopol/index.html'
    context_object_name = 'ports'

class UploadPortView(CreateView):
    model = Port
    fields = ('title', 'pdf', 'cover')
    success_url = reverse_lazy('cpopol:index')
    template_name = 'cpopol/upload.html'

def delete(req,pk):
    if req.method == 'POST':
        port = Port.objects.get(pk=pk)
        port.delete()
        return redirect('cpopol:index')
