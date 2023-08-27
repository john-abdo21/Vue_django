from django.urls import path
from django.conf.urls import include
from .views import CsrfTokenView, LoginView, LogoutView, SessionCheckView


urlpatterns = [
    path(
        "api/",
        include(
            [
                # auth
                path("csrf_token", CsrfTokenView.as_view()),
                path("login", LoginView.as_view()),
                path("logout", LogoutView.as_view()),
                path("session_check", SessionCheckView.as_view()),
            ]
        ),
    )
]
