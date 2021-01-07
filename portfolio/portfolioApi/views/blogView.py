from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from portfolioApi.serializers import BlogSerializer, CategorySerializer
from portfolioApi.models import Category, Blog
from portfolioApi import constants
      
class BlogItems(APIView):
    """
    Portfolio items
    """
    
    permission_classes = (IsAuthenticated)
    def __init__(self):
        pass
    
    # /items?category=Shops&page=1
    @api_view(['GET'])
    def items(request):
        serializer_context = {'request': request}
        
        offset = request.GET.get('page', None)
        category = request.GET.get('category', None)
        
        ''' Validate page param '''
        if offset is None:
            offset = 0
        else:
            if offset.isnumeric() != True:
                raise exceptions.ParseError('Page must be numeric')
            else:
                offset = int(offset)
        
        if category is not None:
            cat = Category.objects.filter(category_name=category)
            results = Blog.objects.filter(category__in=cat).order_by('-published')[offset: offset + 10]
        else: 
            results = Blog.objects.order_by('-published')[offset: offset + 10]
        
        if not results:
            raise exceptions.NotFound()
          
        serializer = BlogSerializer(results, many=True, context=serializer_context)
        return Response(serializer.data)