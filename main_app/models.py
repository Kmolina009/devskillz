from django.db import models
from django.contrib.auth.models import User
from django.urls import rverse 
# Create your models here.
SKILL_LEVELS = (
    (1,"Fundamental Awarness"),
    (2,"Novice"),
    (3,"Intermidiate"),
    (4,"Advanced"),
    (5,"Expert"),
)

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #cascsade keeps the database clean of orphan documents
    skill= models.CharField(max_length=100)
    skill_level = models.IntegerField(
        choices =SKILL_LEVELS,
        default =1
    )

#todo refactor to redirect to index of skill page
def get_absolute_url(self):
    return reverse('home')