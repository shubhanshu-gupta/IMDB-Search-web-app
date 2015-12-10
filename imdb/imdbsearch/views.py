from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from jinja2 import Template
from .forms import NameForm

# def index(request):
# 	template = Template('imdbsearch/url/to/submit/')
# 	return HttpResponse(template.render('index.html'))

def index(request):

	if request.method=='POST':
		#creating a form instance and populating with data from the request
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponse('/result/')

	else:
		form = NameForm()

	return render(request, 'index.html', {'form': form})
