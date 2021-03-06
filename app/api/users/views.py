from rest_framework import viewsets

from api.users.serializers import ProfileDetailSerializers
from api.users.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileDetailSerializers
    queryset = Profile.objects.all()
    authentication_classes = ()
    permission_classes = ()

