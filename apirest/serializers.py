from django.db.models import fields
from rest_framework import serializers
from .models import Asesor


class AsesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Asesor
        fields=['nombres','apellidos','dni','especialidad','celular','email']
        #fields='__all__'