from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from jinja2 import Template
from .forms import NameForm
import jinja2
from jinja2.ext import loopcontrols
jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])
import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import json

# def index(request):
# 	template = Template('imdbsearch/url/to/submit/')
# 	return HttpResponse(template.render('index.html'))

def getunicode(soup):
	body=''
	if isinstance(soup, unicode):
	    soup = soup.replace('&#39;',"'")
	    soup = soup.replace('&quot;','"')
	    soup = soup.replace('&nbsp;',' ')
	    body = body + soup
	else:
	    if not soup.contents:
	        return ''
	    con_list = soup.contents
	    for con in con_list:
	        body = body + getunicode(con)
	return body


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
	celeb_search = '+'.join(celeb.split())

	base_url = 'http://www.imdb.com/find?q='
	url = base_url+celeb_search+'&s=all'

	celebrity_search = re.compile('/name/nm\d+')

	br = Browser()
	br.set_handle_robots(False)

	 
	br.open(url)

#	urllib2.urlopen(url)
	
	link = br.find_link(url_regex = re.compile(r'/name/nm.*'))
	res = br.follow_link(link)

	soup = BeautifulSoup(res.read())

	knownfor=[]
	info = soup.find('div',{'id':'knownfor'})
	r1 = info.find('',{'title':True})['title']
	knownforlist = info.findAll('a',{'href':True})

	for i in range(len(knownforlist)):
		knownfor.append(getunicode(knownforlist[i]))

	title=[]
	for j in range(len(knownfor)):
		title.append(knownfor[j][:-7])

	print 'known for: '
	print ', '.join(knownfor)
	#    for a in info.findAll('a',{'href':True})[1::2]:
	#        print a['href']

	omdb_movie_url=[]
	knownmovie1=[]
	omdb_movie_base_url = 'http://www.omdbapi.com/?i='

	movie_url=[]
	knownmovie=[]
	movie_base_url = 'http://www.imdb.com/title/'

	for a in info.findAll('a',{'href':True})[1::2]:
		movie_url.append(a['href'])

############## Getting the movie title ID from the URL############################
	movie_id = []
	for g in range(len(movie_url)):
		movie_url[g] = movie_url[g][:-16]
		movie_url[g] = movie_url[g][7:]

	movie_id = movie_url
#################################################################################


	for u in range(len(movie_id)):
		omdb_movie_url.append(omdb_movie_base_url+movie_id[u]+'&plot=full&r=json')

###################Fetching reviews######################################################
	imdb_review_url = []
	reviews = []
	for t in range(len(movie_id)):
		imdb_review_url.append(movie_base_url+movie_id[t]+'/reviews?filter=best&spoiler=hide')
		response = urllib2.urlopen(imdb_review_url[t])
		html = response.read()
		soup1 = BeautifulSoup(html)
		rev = soup1.find('div',{'id':'tn15content'})
		reviw = rev.findAll('p')
		for y in range(len(reviw))[:3]:
			reviews.append(getunicode(reviw[y]))
################################################################################################


########################Looping through every movie and printing its detail##############################
		i=0
		finaldata = []
		for g in range(len(omdb_movie_url)):
			data1 = json.load(urllib2.urlopen(omdb_movie_url[g]))
			title = data1['Title']
			poster = data1['Poster']
			movieID = data1['imdbID']
			movieurl = movie_base_url+movieID
			rating = data1['imdbRating']+" from "+data1['imdbVotes']+" votes"
			des = data1['Plot']
			rated = data1['Rated']
			genrelist = data1['Genre']
			release_date = data1['Released']
			runtime = data1['Runtime']
			x = reviews[i:i+3]
			movrev = {}
			for h in range(len(x)):
				movrev = x[h]
			i+=3
			moviedata = {}
			moviedata['name'] = title
			moviedata['poster'] = poster
			moviedata['year'] = release_date
			moviedata['runtime'] = runtime
			moviedata['genre'] = genrelist
			moviedata['rating'] = rating
			moviedata['review'] = movrev
			moviedata['link'] = movieurl
			moviedata['rated'] = rated
			finaldata.append(moviedata)
		template = loader.get_template('imdbsearch/movies.html')
		Context = RequestContext(request, {'finaldata':finaldata})
		print "Final Data ", finaldata
		return HttpResponse(template.render(Context))

#############################################################################################

		
	# for j in range(len(movie_url)):    
	# 	join = urlparse.urljoin(movie_base_url,movie_url[j])
	# 	knownmovie.append(join.encode("UTF-8"))
	# genre=[]
	# data = []
	# for k in range(len(knownmovie)):
	# 	response = urllib2.urlopen(knownmovie[k])
	# 	html = response.read()
	# 	soup1 = BeautifulSoup(html)        
	# 	rate = soup1.find('span',itemprop='ratingValue')
	# 	rating = getunicode(rate)
	# 	des = soup1.find('meta',{'name':'description'})['content']
	# 	infobar = soup1.find('div',{'class':'infobar'})
	# 	r = infobar.find('',{'title':True})['title']
	# 	genrelist = infobar.findAll('a',{'href':True})
	# 	for l in range(len(genrelist)-1):
	# 		genre.append(getunicode(genrelist[l]))
	# 	release_date = getunicode(genrelist[-1])
	# 	review = soup1.find('div',{'class':'user-comments'})
	# 	rev = soup1.find('p', itemprop='reviewBody')
	# 	movie = {}
	# 	movie['name'] = knownfor[k]
	# 	movie['Release Date'] = release_date
	# 	movie['rated'] = r
	# 	movie['description'] = des
	# 	movie['review'] = getunicode(rev)
	# 	data.append(movie)
	# template = loader.get_template('imdbsearch/movies.html')
	# Context = RequestContext(request, {'data':data})
	# print "Final Data ", data
	# return HttpResponse(template.render(Context))