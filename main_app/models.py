from django.db import models
from django.contrib.auth.models import User

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
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField(
        choices =SKILL_LEVELS,
        default =1
    )