from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.pk

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo)
    def __str__(self):
        return self.pk

class Person():
    objects = Manage()
    def __str__(self):
        return 'abc'
class Manage():
    pass
p = Person()
p.age = 18