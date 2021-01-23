from django.shortcuts import render
from django.http import HttpResponseRedirect
from goose3 import Goose 
import tldextract
from unshortenit import UnshortenIt
from .forms import UrlForm


def home(request):
    global data
    data = ''

    global title
    title = ""

    global uri
    uri = ''

    global meta
    meta = ''

    global get_domain
    get_domain = ''
    
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data.get('url')
            form.save()
            form = UrlForm()

            
            unshortener = UnshortenIt()
            uri = unshortener.unshorten(data)

            article = Goose().extract(uri)
            title = article.title
            meta = article.meta_description

            domain = tldextract.extract(uri)

            get_domain = domain.domain + '.' + domain.suffix

            


    else:
        form = UrlForm()

    return render(request, 'unmask/home.html', {'form':form,'ori_link':uri,'title':title,'meta':meta,'domain':get_domain,'data':data})








"""
from unshortenit import UnshortenIt
  if request.method == 'POST':
        
        url = request.POST['shortened_url']
        unshortener = UnshortenIt()
        uri = unshortener.unshorten(url)
        
        print(uri)


shortened_url =None 
uri = None
def home(request):
    global shortened_url
    global uri
  
    else:
        pass
"""