from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
