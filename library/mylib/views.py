from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django import forms
    
from django.template import Context
from django.shortcuts import render_to_response
from mylib.models import Book,Author

# def main(request):
	# return render_to_response("main.html")	

def updata(request):
	book = request.GET["ISBN"]
	if request.POST:
		a = request.POST.get("AuthorID")
		b = Author.objects.get(AuthorID=a)
		post = request.POST
		updatabook = Book.objects.get(ISBN = book)
		updatabook.ISBN = post["ISBN"]
		updatabook.Title = post["Title"]
		updatabook.AuthorID = b
		updatabook.Publisher = post["Publisher"]
		updatabook.PublishDate = post["PublishDate"]
		updatabook.Price = post["Price"]
		updatabook.save()
	return render_to_response("updata_book.html", {'book': Book.objects.get(ISBN=book)})
	
def search_result(request):
	if "search" in request.POST:
		post = request.POST
		tmp = Author.objects.filter(Name = post["search"])
		if tmp:
			books = tmp[0].book_set.all()
			return render_to_response("search_result.html", locals())
		else:
			return render_to_response("error2.html")
		
# def search_author(request):
	# return render_to_response("search_author.html")
	
def books(request):
	books = Book.objects.all()
	return render_to_response("books.html", locals())
	
def del_book(request):
	book = request.GET["ISBN"]
	b = Book.objects.get(ISBN = book)
	b.delete()
	books = Book.objects.all()
	return render_to_response("books.html", locals())

def add_author(request):
	if request.POST:
		post = request.POST
		author = Author(
			AuthorID = post["AuthorID"],
			Name = post["Name"],
			Age = post["Age"],
			Country = post["Country"],
		)
		author.save()
	return render_to_response("add_author.html", locals())
	
def add_book(request):
	if request.POST:
		a = request.POST.get("AuthorID")
		author = Author.objects.filter(AuthorID=a)
		if author:
			post = request.POST
			book = Book(
				ISBN = post["ISBN"],
				Title = post["Title"],
				AuthorID = author[0],
				Publisher = post["Publisher"],
				PublishDate = post["PublishDate"],
				Price = post["Price"],
			)
			book.save()
		else:
			return render_to_response("error.html")		
	return render_to_response("add_book.html", locals())

def book_information(request):
	bookid = request.GET["ISBN"]
	book = Book.objects.get(ISBN = bookid)
	return render_to_response("book_information.html", locals())