from django.db import models

# Create your models here.


class Header(models.Model):

    topic = models.CharField("Header Topic", max_length = 60)
    text = models.TextField('Header Text')
    image = models.ImageField("Header image", upload_to='images/')
    button_text = models.CharField("Header Button text", max_length = 40)

    def __str__(self) -> str:
        return self.topic
    


class About(models.Model):

    topic = models.CharField('About Topic', max_length = 100)
    text1 = models.TextField('About Text 1')
    text2 = models.TextField('About Text 2')
    image = models.ImageField("About image", upload_to='images/')
    button_text = models.CharField("About button text", max_length = 50)


    def __str__(self) -> str:
        return self.topic
    

class Service(models.Model):

    service_topic = models.CharField("Service topic", max_length = 60)
    text = models.TextField("Service text", blank=True, null=True)
    image = models.ImageField("Service image", upload_to='images/')
    

    def __str__(self) -> str:
        return self.service_topic


class Price(models.Model):

    image = models.ImageField("Service image", upload_to = 'images/')
    topic = models.CharField("Service topic", max_length = 60)
    price = models.FloatField("Service price")

    def __str__(self) -> str:
        return self.topic
    

class Contact(models.Model):

    name = models.CharField("Customer name", max_length = 70)
    phone = models.CharField("Customer phone", max_length = 20)
    email = models.EmailField("Customer email")
    subject = models.CharField("Message Subject", max_length = 80)
    message = models.TextField("Customer message")

    def __str__(self) -> str:
        return self.subject


class Portfolio(models.Model):

    image = models.ImageField("Work Image", upload_to='images/')

    

class Team(models.Model):

    image = models.ImageField("Worker image", upload_to='images/')
    name = models.CharField("Worker name", max_length = 90)
    proffession = models.CharField("Worker proffession", max_length = 70)

    def __str__(self) -> str:
        return self.name
    
