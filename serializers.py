from rest_framework import serializers
from .models import movie,collection

class movieSerializer(serializers.ModelSerializer):
   class Meta:
       model=movie
       fields = ['title','discription','genres','id']


class collectionSerializer(serializers.ModelSerializer):
    class Meta :
        model = collection
        fields= ['title','discription','movie','collection_id']