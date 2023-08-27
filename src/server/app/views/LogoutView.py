from core.views import APIView
from django.contrib.auth import logout
from django.http import JsonResponse


class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return JsonResponse(data={"message": "Successfully logged out."}, status=200)
