from django.db import models
import uuid
# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=300)
    discription=models.CharField(max_length=300)
    genres=models.CharField(max_length=300)
    id=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    def __str__(self):
        s = str(self.title)
        return (s)



class collection(models.Model):
    title=models.CharField(max_length=300)
    discription=models.CharField(max_length=300)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    collection_id =models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

