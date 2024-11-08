# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer
from projects.models import Pledge
from projects.serializers import PledgeSerializer
from .permissions import IsUserOrAdminOnly


class CustomUserList(APIView):
    def get_permissions(self):
        # Override this method to apply different permissions for different HTTP methods.
        if self.request.method == "GET":
            return [permissions.IsAuthenticated() ,permissions.IsAdminUser()]
        elif self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get(self, request):
        users = CustomUser.objects.all()
        self.check_object_permissions(request, users)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrAdminOnly
    ]
        
    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance = user,
            data = request.data,
            partial = True,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
        serializer.errors,
        status = status.HTTP_404_NOT_FOUND
        )
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user_id": user.id, "email": user.email})


class CustomUserPledgeList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUserOrAdminOnly]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        user_pledges = user.pledges.all()
        serializer = PledgeSerializer(user_pledges, many=True)
        return Response(serializer.data)
