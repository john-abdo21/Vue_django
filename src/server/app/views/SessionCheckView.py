from django.views import View
from django.http import JsonResponse
from app.presenters.user import create_authenticated_user_data


class SessionCheckView(View):
    def get(self, request):
        user = request.user

        if user.is_authenticated:
            return JsonResponse(
                data=create_authenticated_user_data(user),
                status=200,
            )

        return JsonResponse(data={"isAuthenticated": False}, status=200)
