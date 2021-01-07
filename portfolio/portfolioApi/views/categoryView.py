from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from portfolioApi.serializers import CategorySerializer
from portfolioApi.models import Category
from portfolioApi import constants

class CategoryItems(APIView):
    """
    Category items
    """
    
    permission_classes = (IsAuthenticated)
    
    def __init__(self):
        pass
    
    # categories
    @api_view(['GET'])
    def categories(request):
        results = Category.objects.order_by('-pub_date')
        if not results:
            raise exceptions.NotFound()
        serializer = CategorySerializer(results, many=True)
        return Response(serializer.data)