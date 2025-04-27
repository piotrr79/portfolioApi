from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from portfolioApi.serializers import ArticleSerializer
from portfolioApi.models import Article

class ArticleItems(APIView):
    """
    ArticleItems class
    """
    
    permission_classes = (IsAuthenticated)
    
    def __init__(self):
        pass
    
    # article?title=Contact
    @api_view(['GET'])
    def article(request):
        title = request.GET.get('title', None)
        if title is None or title == '':
            raise exceptions.ParseError('Request url is missing title query param')
        
        results = Article.objects.filter(title__contains=title)
        if not results:
            raise exceptions.NotFound()
        serializer = ArticleSerializer(results, many=True)
        return Response(serializer.data)
