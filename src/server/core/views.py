from django.views.generic import View
from rest_framework.views import APIView
from django.db import models


class APIView(APIView, View):
    @classmethod
    def as_view(cls, **initkwargs):
        """
        Store the original class on the view function.

        This allows us to discover information about the view when we do URL
        reverse lookups.  Used for breadcrumb generation.
        """
        if isinstance(getattr(cls, "queryset", None), models.query.QuerySet):

            def force_evaluation():
                raise RuntimeError(
                    "Do not evaluate the `.queryset` attribute directly, "
                    "as the result will be cached and reused between requests. "
                    "Use `.all()` or call `.get_queryset()` instead."
                )

            cls.queryset._fetch_all = force_evaluation

        view = super().as_view(**initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs

        return view
