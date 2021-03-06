import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category,Page

def populate():
    pyviews = 128
    pylikes = 64
    djviews = 64
    djlikes = 32
    oviews = 32
    olikes = 16

    python_pages = [{
    'title': 'Official Python Tutorial',
    'url': 'http://docs.python.org/3/tutorial/',
     'views': 20},
    {'title':'How to Think like a Computer Scientist',
    'url':'http://www.greenteapress.com/thinkpython/',
    'views': 30},
    {'title':'Learn Python in 10 Minutes',
    'url':'http://www.korokithakis.net/tutorials/python/',
    'views': 100}]
    django_pages =[
    {'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
    'views': 10},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/',
    'views': 15},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/',
    'views': 28}]

    other_pages = [{'title':'Bottle',
    'url':'http://bottlepy.org/docs/dev/',
    'views': 70},
    {'title':'Flask',
    'url':'http://flask.pocoo.org',
    'views': 30}]


    cats = {'Python': {'pages': python_pages, 'views': pyviews, 'likes': pylikes},
    'Django': {'pages': django_pages, 'views': djviews, 'likes':djlikes},
    'Other Frameworks': {'pages': other_pages, 'views': oviews, 'likes': olikes} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category = cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views,like):
    c = Category.objects.get_or_create(name = name) [0]
    c.likes = like
    c.views = views
    c.save()
    return c

if __name__ == '__main__':
    print("Starting rango popukation script...")
    populate()