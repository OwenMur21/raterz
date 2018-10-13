from rest_framework import serializers
from .models import Profile, Project

class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'user')

