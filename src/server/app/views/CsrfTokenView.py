from rest_framework.response import Response
from rest_framework.views import APIView
from django.middleware.csrf import get_token


class CsrfTokenView(APIView):
    def get(self, request):
        return Response({"token": get_token(request)}, 200)
