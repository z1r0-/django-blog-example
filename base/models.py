from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor import fields


class Tag(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Entwurf'),
        ('publish', 'Veröffentlicht'),
        ('trash', 'Gelöscht')
    )

    title = models.CharField('Titel', max_length=255)
    content = fields.RichTextField('Inhalt')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    publish = models.DateTimeField('Veröffentlichungs-Datum', default=timezone.now)
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=10)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    email = models.EmailField('Email')
    homepage = models.URLField('Homepage', blank=True, null=True)
    text = models.TextField('Text')
    post = models.ForeignKey(Post, related_name='comments')
    date = models.DateTimeField('Datum', default=timezone.now, editable=False)

