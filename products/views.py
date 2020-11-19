from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'price', 'code']
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Products.objects.all()
        else:	
            return Products.objects.filter(seller=user)
    
    def perform_create(self, ProductSerializer):
        ProductSerializer.save(seller=self.request.user)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
