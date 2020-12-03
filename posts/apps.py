from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'


class MyMiddlewareOne:
    def __init__(self,get_response):
        self.get_response = get_response
        print(self.__class__.__name__+" Instance Created")
        pass

    def __call__(self, request):
        response = self.get_response(request)
        print('**********Debuging********')
        print(response.__class__.__name__)
        print('**********Debuging********')
        return response
