from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        tokens = serializer.get_tokens(user)
        return Response(tokens, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Follow a user."""
        try:
            user_to_follow = User.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.add(user_to_follow)
            return Response({"message": "User followed successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Unfollow a user."""
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            if user_to_unfollow == request.user:
                return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

            request.user.following.remove(user_to_unfollow)
            return Response({"message": "User unfollowed successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class FollowersListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get followers of a specific user."""
        user_id = self.kwargs["user_id"]
        try:
            return User.objects.get(id=user_id).followers.all()
        except User.DoesNotExist:
            return User.objects.none()

class FollowingListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Get users that a specific user is following."""
        user_id = self.kwargs["user_id"]
        try:
            return User.objects.get(id=user_id).following.all()
        except User.DoesNotExist:
            return User.objects.none()