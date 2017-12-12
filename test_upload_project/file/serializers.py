from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    cover_x256 = serializers.SerializerMethodField()

    def get_cover_x256(self, obj):
        return obj.cover_x256.url

    class Meta:
        model = Profile
        fields = '__all__'
