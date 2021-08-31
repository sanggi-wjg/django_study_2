from django.contrib.auth.models import User, Group
from rest_framework import serializers

from sample.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SampleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class SampleGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 100, allow_blank = True, required = False)
    code = serializers.CharField(style = { 'base_template': 'textarea.html' })
    linenos = serializers.BooleanField(required = False)
    language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
    style = serializers.ChoiceField(choices = STYLE_CHOICES, default = 'friendly')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
