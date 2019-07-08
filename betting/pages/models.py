from django.db import models

# Create your models here.
class GameInfo(models.Model):
    temp_id = models.IntegerField()
    first_name  =  models.CharField(max_length=20,blank=True)
    last_name  =  models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=1)
    ranking = models.IntegerField()
    age = models.IntegerField()
    singles = models.BooleanField(default=False)
    doubles = models.BooleanField(default=False)
    mix_double = models.BooleanField(default=False)

    all_mix_double = models.BooleanField(default=False)
    def  __str__(self):
        return self.first_name + " "+self.last_name
