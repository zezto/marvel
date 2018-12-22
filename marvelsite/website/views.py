from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Contacts
from.forms import ContactForm
# Create your views here.


def index(request):
    a = Article.objects.all()
    context = {'a': a}
    return render(request, 'website/index.html', context=context)


def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def detail(request, article_id):
    a = Article.objects.get(pk=article_id)
    context = {'a': a}
    return render(request, 'website/details.html', context=context)

def comments(request):
    com = Contacts.objects.all()
    context = {'com': com}
    return render(request, 'website/comments.html', context=context)

