from django.shortcuts import render
from django.http import HttpResponse
from first.models import *

# Create your views here.
def home(reqeust):
    return HttpResponse("this is what")

def hello(request):
    contents = {
        "para":"is it django?",
    }
    return render(request, 'first/hello.html', contents)

def create(request):
    new_post = Notebook(note_data="aa")
    new_post.save()
    return render(request, )

def get_note(request):
    note = Notebook.objects.all()
    context = {'lists':note}
    return render(request, 'first/get_note.html', context)