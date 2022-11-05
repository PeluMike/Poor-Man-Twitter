from symbol import decorator, decorators
from telnetlib import STATUS
from rest_framework.decorators import api_view
from .models import TwitterApp
from .serializer import TwitterSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def index(request):
    tweets = TwitterApp.objects.all().order_by('-dateCreated')
    serializer = TwitterSerializer(tweets, many= True)
    serializer_data = serializer.data
    final_data = []
    for i, tweet in enumerate(tweets):
        edit_serializer = serializer_data[i]
        edit_serializer["dateCreated"] = tweet.dateCreated.strftime("%m/%d/%Y, %H:%M:%S")
        final_data.append(edit_serializer)
        
    
    return Response(final_data, status=status.HTTP_200_OK)
    

@api_view(['POST']) 
def create(request):
    if request.method == 'POST':
        serializer = TwitterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    