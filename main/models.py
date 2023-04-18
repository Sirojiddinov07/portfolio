from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='media/')
    link =  models.URLField(null=True, blank=True)
    exralink = models.URLField(null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()

class Services(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)

class About(models.Model):
    img = models.ImageField(upload_to='media/')
    inform = models.TextField()



class Friends(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=200)
    inform = models.TextField()



class Blog(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=200)
    inform = models.TextField()
    extra = models.TextField()
