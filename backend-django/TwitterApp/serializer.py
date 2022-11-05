

#
#

from pyexpat import model
from rest_framework import serializers
from .models import TwitterApp




class TwitterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TwitterApp
        fields = "__all__"
    