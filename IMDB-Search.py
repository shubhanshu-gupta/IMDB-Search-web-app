
# coding: utf-8

# In[43]:




# In[23]:

import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup
from mechanize import Browser
import re
import json

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


def main():
    celeb = str(raw_input('Celebrity Name: '))
    celeb_search = '+'.join(celeb.split())
    
    base_url = 'http://www.imdb.com/find?q='
    url = base_url+celeb_search+'&s=all'
    
    celebrity_search = re.compile('/name/nm\d+')
    
    br = Browser()
    br.set_handle_robots(False)
    
                     
    br.open(url)

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
    print ', '.join(title)
    
#    for a in info.findAll('a',{'href':True})[1::2]:
#        print a['href']
    
    testurl = "http://www.omdbapi.com/?i=tt1187043&plot=full&r=json"
    data = json.load(urllib2.urlopen(testurl))
    
#    print data['Genre']
    
    omdb_movie_url=[]
    knownmovie1=[]
    omdb_movie_base_url = 'http://www.omdbapi.com/?i='
    
#    for u in range(len(title))[1::2]:
#        omdb_movie_url.append(omdb_movie_base_url+title[u]+'&y=&plot=short&r=json')
        
#    for g in range(len(omdb_movie_url)):
#        data1 = json.load(urllib2.urlopen(omdb_movie_url[g]))
#        print 'Genre of each movie: '
#        print ', '.join(data1)
#        print omdb_movie_url[g]
    
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
#        print movie_url[g]
#################################################################################    
    movie_id = movie_url
    
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
    
    print len(reviews)
                   
########################Looping through every movie and printing its detail##############################    
    for g in range(len(omdb_movie_url)):
        data1 = json.load(urllib2.urlopen(omdb_movie_url[g]))
        poster = data1['Poster']
        rating = data1['imdbRating']+" from "+data1['imdbVotes']+" votes"
        des = data1['Plot']
        rated = data1['Rated']
        genrelist = data1['Genre']
        release_date = data1['Released']
        print data1['Title']
        print 'Released On: ', release_date
        print poster
        print 'Rating: ', rating
        print 'Rated: ', rated
        print 'Runtime: ', data1['Runtime']
        print ''
        print 'Genre: ', genrelist
        print '\nDescription:'
        print  des
        print ''
        print '\n 3 Best Reviews:'
        for n in range(len(reviews)):
            print 'Review number'+ str(n)+': '
            print  reviews[n]
            print ''
        print ''

#############################################################################################

#        print data1
#        print 'Genre of each movie: '
#        print ', '.join(data1['Genre'])
#        print omdb_movie_url[g]

    
#    for j in range(len(movie_url)):    
#        join = urlparse.urljoin(movie_base_url,movie_url[j])
#        knownmovie.append(join.encode("UTF-8"))
        
    
#    print knownmovie
#    print knownmovie
#    genre=[]
    
#    for k in range(len(knownmovie)):
#        response = urllib2.urlopen(knownmovie[k])
#        html = response.read()
#        soup1 = BeautifulSoup(html)        
#        rate = soup1.find('span',itemprop='ratingValue')
#        rating = getunicode(rate)
#        des = soup1.find('meta',{'name':'description'})['content']
#        infobar = soup1.find('div',{'class':'infobar'})
#        r = infobar.find('',{'title':True})['title']
#        r = infobar.find('meta', itemprop='contentRating') 
#        genrelist = infobar.findAll('a',{'href':True})
#        for l in range(len(genrelist)-1):
#            genre.append(getunicode(genrelist[l]))
#        release_date = getunicode(genrelist[-1])
#        review = soup1.find('div',{'class':'user-comments'})
#        rev = soup1.find('p', itemprop='reviewBody')
       # print movie_title,rating+'/10.0'
#        print 'Release Date:',release_date
#        print 'Rated',r
#        print ''
#        print 'Genre:',
#        print ', '.join(genre)
#        print '\nDescription:'
#        print des
#        print '\nReview:'
#        print getunicode(rev)
#        print ''
#        print ''
    
            
#    movie_title = getunicode(soup.find('title'))
#    rate = soup.find('span',itemprop='ratingValue')
#    rating = getunicode(rate)
    
#    actors=[]
#    actors_soup = soup.findAll('a',itemprop='actors')
#    for i in range(len(actors_soup)):
#        actors.append(getunicode(actors_soup[i]))
    
#    des = soup.find('meta',{'name':'description'})['content']

#    genre=[]
#    infobar = soup.find('div',{'class':'infobar'})
#    r = infobar.find('',{'title':True})['title']
#    genrelist = infobar.findAll('a',{'href':True})
    
#    for i in range(len(genrelist)-1):
#        genre.append(getunicode(genrelist[i]))
#    release_date = getunicode(genrelist[-1])

#    review = soup.find('div',{'class': 'user-comments'})
#    rev = soup.find('p', itemprop='reviewBody')
    
#    print movie_title,rating+'/10.0'
#    print 'Relase Date:',release_date
#    print 'Rated',r
#    print ''
#    print 'Genre:',
#    print ', '.join(genre)
#    print '\nActors:',
#    print ', '.join(actors)
#    print '\nDescription:'
#    print des    
#    print '\nReview:'
#    print rev
#    print r1
#    print 'knownfor:',
#    print ', '.join(knownfor)
    
if __name__ == '__main__':
    main()


# In[ ]:


# In[ ]:



