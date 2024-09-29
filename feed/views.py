from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductFeedView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer