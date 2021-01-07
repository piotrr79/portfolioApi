from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
 
class PortfolioHome(APIView):
    """
    Main url welcome message
    """
    permission_classes = (IsAuthenticated)
    def __init__(self):
        pass
    
    @api_view(['GET'])
    def index(request):
        return Response('Portfolio Api')