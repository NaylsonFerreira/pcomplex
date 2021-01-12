from django.conf import settings


def core_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        request.default_app = settings.DEFAULT_APP
        request.default_app_label = settings.DEFAULT_APP_LABEL

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
