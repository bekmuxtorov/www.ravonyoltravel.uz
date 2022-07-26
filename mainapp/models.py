from audioop import reverse
from distutils.command.upload import upload
from email.policy import default
from turtle import update
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Travel(models.Model):
    qayerdan = models.CharField(max_length=50, verbose_name= "Qayerdan:")
    qayerga = models.CharField(max_length=50, verbose_name = "Qayerga:")
    picture = models.ImageField(blank = True, verbose_name = "Rasmni joylang:")
    qisqa_mal = models.TextField(verbose_name = "Qisqacha ma'lumot:")
    davomiyligi = models.CharField(max_length=20, verbose_name = "Sayohat davomiyligi:")
    narxi = models.CharField(max_length=20,verbose_name = "Sayohat narxi")
    toliq_mal = RichTextField(verbose_name="To'liq ma'lumot:")

    def __str__(self):
        return f"{self.qayerdan} {self.qayerga}"


class Tassurotlar(models.Model):
    sarlavha = models.CharField(max_length=50, verbose_name='Sarlavha')
    qisqa_mal = models.CharField(max_length=200, verbose_name = "Qiqacha ma'lumot")
    picture = models.ImageField(blank = True, verbose_name = "Rasmni joylang:")
    toliq_mal = RichTextField(verbose_name="To'liq ma'lumot")

    def __str__(self):
        return self.sarlavha
    
    def get_absolute_url(self):
        return reverse('news_detail', args = [str(self.pk)])

class Rasmlar(models.Model):
    image = models.ImageField(blank = True, verbose_name = 'Rasmni joylang:')
    name = models.CharField(max_length = 20, verbose_name= 'Rasmning nomi:')

    def __str__(self):
        return self.name


class Fikrlar(models.Model):
    name = models.CharField(max_length=70, verbose_name = 'Ism, familiyangizni kiriting: ')
    text = models.TextField(max_length=300, verbose_name= 'Fikrlaringizni kiriting: ')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fikrlar_detail', args = [str(self.pk)])

class Transport(models.Model):
    name = models.CharField(max_length=30, verbose_name="Transport nomini kiriting:")
    image = models.ImageField(blank= True, verbose_name="Transport rasmini joylang: ")

    def __str__(self):
        return self.name










