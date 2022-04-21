from dataclasses import field
from operator import mod
from pyexpat import model
from me.models import Tag, Work, About
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
