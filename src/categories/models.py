from django.db import models
from rest_framework import serializers

class Category(models.Model):
    name = models.CharField(max_length=60)



# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
