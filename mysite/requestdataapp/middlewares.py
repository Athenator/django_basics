from django.http import HttpRequest


def set_usergaent_on_request_middleware(get_response):
    print('initial call')

    def middleware(request: HttpRequest):
        print('before get response')
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print('after get response')
        return response

    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0
        self.responses_count = 0
        self.exception_count = 0

    def __call__(self, request: HttpRequest):
        self.request_count += 1
        print("request count", self.responses_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("request count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exception_count += 1
        print('got', self.exception_count, 'exceptions so far')
