from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
# Author {AuthorID (PK), Name, Age, Country}
class Author(models.Model):
	AuthorID = models.CharField(primary_key = True, max_length = 30)
	Name = models.CharField(max_length = 30)
	Age = models.CharField(max_length = 10)
	Country = models.CharField(max_length = 30)
	
class Book(models.Model):
	#user = models. ForeignKey(User)
	ISBN = models.CharField(primary_key = True, max_length = 30)
	Title = models.CharField(max_length = 50)
	AuthorID = models.ForeignKey(Author)
	Publisher = models.CharField(max_length = 50)
	PublishDate = models.CharField(max_length = 20)
	Price = models.CharField(max_length = 20)
	

	