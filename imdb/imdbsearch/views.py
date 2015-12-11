from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from jinja2 import Template
from .forms import NameForm
import jinja2
from jinja2.ext import loopcontrols
jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

# def index(request):
# 	template = Template('imdbsearch/url/to/submit/')
# 	return HttpResponse(template.render('index.html'))

def index(request):
	form = NameForm()
	template = loader.get_template('imdbsearch/index.html')
	Context = RequestContext(request, {'form': form})
	return HttpResponse(template.render(Context))

	# query = request.GET['q']
	# t = loader.get_template('imdbsearch/index.html')
	# c = Context({ 'query' : query,})
	# return HttpResponse(t.render(c))

	# if request.method=='POST':
	# 	#creating a form instance and populating with data from the request
	# 	form = NameForm(request.POST)
	# 	if form.is_valid():
	# 		return HttpResponse('/result/')

	# else:
	# 	form = NameForm()

	# return render(request, 'index.html', {'form': form})

def show(request):
	print "sdgfds"
	celeb = request.POST['celeb_name']
	print celeb