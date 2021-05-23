from rest_framework import viewsets
from .models import Category, CategorySerializer


from rest_framework.settings import api_settings


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
