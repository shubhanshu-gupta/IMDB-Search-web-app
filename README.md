# IMDB-Search-web-app
This web app enables a user to search for an actor's/actress's top known movies along with their respective details like user reviews, ratings, runtime, release date, movie poster, etc. 

I have followed the directory structure and workflow of Django framework of python language. Inside the project called “imdb”, there is an app named “imdbsearch”. The UI templates are placed in imdb/imdbsearch/templates/imdbsearch. Twitter Bootstrap is used to implement the frontend pages.

Some of the important files with respect to the project – (imdb/imdbsearch) - for better understanding of the workflow, are:
###Forms.py 
This creates a NameForm class, that is used in subsequent scripts, which houses a text search box.

###Views.py
All the main backend functions are written here. Data is rendered through the HTTPResponse, using the django templating language, and when a particular function is called, data is loaded in to the html files defined within the function. In this, we declare the context in the session before redirecting. The target view picks up the context from the session and renders the template. 

###Urls.py
URL calls to different functions are mentioned in this file.

There are mainly two pages. First page (index.html) is a form to enter the name of the celebrity (actor/actress). Second page (movies.html) is the result page where relevant results are shown as per the input from the user. Then, there are two primary functions in the views.py script. First, index - it basically loads the form template(created in forms.py) in the index.html file. Second, show - it is called as a result of the input submitted by the user in the index.html file. The name of the celebrity is retrieved and then the entire logic of crawling the IMDB website for reviews is written here. It then passes the moviedata as context to the movies.html template.

As soon as the main (home) page loads, it is the index function working there and when the form is submitted /imdbsearch/show URL gets loaded, defined in the urls.py file. 


##INSTRUCTIONS
It briefs the instructions for setting up the project locally.
I have implemented the project in python language using the django web-framework.
Following are the instructions to set up the project locally:
1. Pre-requisites : Python version 2.7/3.4/3.5, Django version 1.9
2. Download the zip folder (named – “ IMDB-Search-web-app ”) or clone from github (https://github.com/shubhanshu-gupta/IMDB-Search-web-app)
3. Go to the directory where you have manage.py file (Do C:\Users\Shubhanhu\> cd imdb)
4. Now, run the server by this command: python manage.py runserver (Write like this: C:\Users\Shubhanhu\> python manage.py runserver)
5. It will automatically check for errors like indentations, missing data and other problematic things. Once, all sorted out and running: go to the server path http://127.0.0.1:8000/ from any web server (preferably chrome).
6. The IMDB-Search-web-app is fired to life.
 

##REFERENCES
It briefs the external libraries/open source projects that helped me build this project.
1. Twitter Bootstrap (Directly used from the source: http://getbootstrap.com/)
2. Bootstrap3 for Django (https://github.com/dyve/django-bootstrap3)
3. OMDB API (http://www.omdbapi.com/)
4. BeautifulSoup for parsing and Mechanize for browser calls
5. Django templating language












