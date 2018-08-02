from django.db import models
from django.contrib.auth.models import User


class Bulletin(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    url = models.TextField(blank=True)
    votes_total = models.IntegerField(default=1)
    pub_date = models.DateTimeField()

    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %m %y')
