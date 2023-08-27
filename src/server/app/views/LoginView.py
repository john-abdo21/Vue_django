from django.views import View
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
from app.presenters.user import create_authenticated_user_data


class LoginView(View):
    def post(self, request):
        params = json.loads(request.body)
        login_id = params.get("loginId")
        password = params.get("password")
        user = authenticate(username=login_id, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse(
                data=create_authenticated_user_data(user),
                status=200,
            )

        return JsonResponse(data={"isAuthenticated": False}, status=403)
