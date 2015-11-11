from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from models import book,author
import MySQLdb
from django import forms

# Create your views here.
def catlog(request):
    return render_to_response('catlog.html')
    
def first(request):
    return render_to_response('first.html')
    
def sear(request):
    return render_to_response('sear.html')
    
def showall(request):##template??
    book_lst = book.objects.all()
    if book_lst:
        return render_to_response('showall.html',{'book_lst':book_lst})
    else:
        message="Sorry! No book in database."
        return render_to_response('success.html',{'message':message})

def search(request):
    #print request.POST
    if request.POST:
        author_lst = author.objects.filter(name__contains = request.POST['authorname'])#accrding name
        if author_lst:
            author_lst=author_lst[0]
            book_lst = book.objects.filter(authorid__contains = author_lst.authorid)
        if author_lst:
            if book_lst:
                return render_to_response('search.html',{'book_lst': book_lst})#
            else:
                message="Sorry! This author has no book in database."
                return render_to_response('success.html',{'message':message})
        else:
            message="Sorry! This author not in database."
            return render_to_response('success.html',{'message':message})
    else:
        return render_to_response('sear.html')
    
def images(request):
    return HttpResponse(open('images/'+request.GET['id'],'rb'),mimetype='image/jpeg')

def add(request):
    return render_to_response('add.html')

def addbook(request):#edit
    if request.POST:
        post=request.POST
        authorid=post['authorid']
        multiple_book = book(ISBN = post['ISBN'],title = post['title'],authorid = authorid, publisher=post['publisher'],publishdate=post['publishdate'],
                             price=post['price'])
        multiple_book.save()
        try:#
            author_lst = author.objects.filter(authorid__contains = authorid)
            if author_lst:
                message="Congratulation! Operation success."
                return render_to_response('success.html',{'message':message})
            else:
                return render_to_response('authorad.html',{'authorid':authorid})
        except:
            return render_to_response('authorad.html',{'authorid':authorid})
    else:
        return render_to_response('add.html')

def delete(request):
    if 'id' in request.GET:
#        delete from Book where book.title=book.title;
        n_book_lst = book.objects.filter(title = request.GET['id'])
        n_book_lst.delete()
    message="Congratulation! Operation success."
    return render_to_response('success.html',{'message':message})

def update(request):
    if 'id' in request.GET:
        book_lst = book.objects.get(title = request.GET['id'])
        #author_lst=author.objects.get(id=int(book_lst.authorid))
    if request.POST:
        post = request.POST
        authorid = post['authorid']
        book_lst = book(ISBN = post['ISBN'],title = post['title'],authorid = authorid, publisher=post['publisher'],publishdate=post['publishdate'],
                             price=request.POST['price'])
        book_lst.save()
        book_lst=book.objects.all()
        try:
           author_lst = author.objects.filter(authorid__contains = authorid) 
           if author_lst:
               message="Congratulation! Operation success."
               return render_to_response('success.html',{'message':message})
           else:
               return render_to_response('authorad.html',{'authorid':authorid})
        except:
    #if author.objects.get('author.name')
            return render_to_response('authorad.html',{'authorid':authorid})
    return render_to_response('update.html',{'book':book_lst})##
def authorad(request):
    #author.name no 
    if request.POST:
        author_lst=author(authorid=request.POST['authorid'],name=request.POST['name'],age=request.POST['age'],country=request.POST['country'])
        author_lst.save()
        message="Congratulation! Operation success."
        return render_to_response('success.html',{'message':message})
    else:
        return render_to_response('authorad.html')
    
def showdata(request):
    if 'id' in request.GET:
        book_lst = book.objects.get(title = request.GET['id'])
        author_lst = author.objects.get(authorid = book_lst.authorid)
        return render_to_response('showdata.html',{'book':book_lst,'author':author_lst})#author

