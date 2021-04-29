from rest_framework import serializers
from restauth.models import Mods
from django.contrib.auth.models import User


# output serializer class for  'Mods' model
class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mods
        fields = '__all__'