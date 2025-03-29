from django.http import JsonResponse
from django.views import View

class UserFeedView(View):
    def get(self, request):
        return JsonResponse({"message": "User feed response"})