import json
import traceback
from logging import getLogger
from django.http import JsonResponse


class RequestDetailLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, _, __, ___):
        logger = getLogger(__name__)
        user = request.user
        params = json.loads(request.body) if request.body else None
        logger.info(f"{request.path} {request.method} user={user}, params={params}")
        return None


class RequestExceptionLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, e):
        logger = getLogger(__name__)
        user = request.user
        params = json.loads(request.body) if request.body else None
        traceback_ = traceback.format_exc()
        logger.error(
            f"{request.path} {request.method} user={user}, params={params}, exception={e}\n{traceback_}"
        )
        return JsonResponse(
            data={
                "exception": traceback.format_exception_only(type(e), e)[0],
                "traceback": traceback_,
            },
            status=403,
        )
