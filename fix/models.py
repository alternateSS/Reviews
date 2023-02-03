from django.db import models


class RequestBugs(models.Model):
    statuses = (
        ('несрочно', 'несрочно'),
        ('средний приоритет', 'средний приоритет'),
        ('срочно', 'срочно'),
        ('немедленно к исправлению', 'немедленно к исправлению')
    )
    problem = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=statuses)
    date = models.DateTimeField(auto_now_add=True)


class Files(models.Model):
    file = models.FileField(upload_to='file', blank=True, null=True, verbose_name='Файл')
    requst_bugs = models.ForeignKey(RequestBugs, blank=True, null=True, on_delete=models.CASCADE, related_name='bugs')