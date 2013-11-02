from django.db import models
import datetime


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
      return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())

    def get_absolute_url(self):
        cur = connection.cursor()
        cur.execute(
            "SELECT id FROM library_book WHERE title = %s",
            [self.title])
        return "/library/books/%s/" % cur.fetchall()[0]

    def __unicode__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.website)
