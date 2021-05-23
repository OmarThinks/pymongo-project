from django.db import models
from rest_framework import serializers

class Category(models.Model):
    name = models.CharField(max_length=60)
    parent = models.ForeignKey("self", null=True, 
    	blank=True, on_delete = models.SET_NULL, 
    	related_name='children')









# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"