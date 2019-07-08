from django.http import HttpResponse
from django.http import HttpResponseRedirect


class m1:
    def process_request(self, request):
        # print(request.META)
        username = request.session.get("username")
        print(username, 'username')
        path_info = request.META.get("PATH_INFO")
        print(path_info)
        if not username:
            if '/static/' in path_info:
                if not path_info.endswith('login.html'):
                    return HttpResponseRedirect('/static/login.html')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("after process_request befor into view")

    def process_response(self, request, response):
        print("this is process_response")
        return response

    def process_exception(self, request, exception):
        print('this is process exception...')
