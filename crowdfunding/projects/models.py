from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="owned_projects"
    )

    def __st__(self):
        return self.title

    @property
    def pledge_sum(self):
        pledges = self.pledges.all()
        sum = 0
        for pledge in pledges:
            sum += pledge.amount
        return sum


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="pledges"
    )
    
    supporter = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="pledges", null=True, blank=True
    )

    def __str__(self):
        return f'{self.amount} pledged to {self.project.title}'