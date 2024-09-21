from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    user_id = models.IntegerField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)


class ItemsSubmitted(models.Model):
    item_id = models.IntegerField(max_length=30)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey


class PledgesMade(models.Model):
    pledge_id = models.IntegerField(max_length=30)
    pledge_amount = models.FloatField
    first_name = models.ForeignKey
    last_name = models.ForeignKey
    email = models.ForeignKey
    item_id = models.ForeignKey
