from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # 🔐 PROTECTION ACTIVÉE

    def get_queryset(self):
        queryset = User.objects.all()

        # 🔍 récupération des params
        name = self.request.query_params.get('name')
        email = self.request.query_params.get('email')

        # 🔍 filtre par name
        if name:
            queryset = queryset.filter(name__icontains=name)

        # 🔍 filtre par email
        if email:
            queryset = queryset.filter(email__icontains=email)

        return queryset