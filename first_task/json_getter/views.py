from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest

from django.views.decorators import csrf


@csrf.csrf_exempt
def example_getter(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return JsonResponse(
            [{"p": f"1:2:3:{i}", "v": "1,234"} for i in range(4, 99 + 1)],
            safe=False)
    else:
        return HttpResponse(f"Bad request with HTTP {request.method} method.", status=405)


@csrf.csrf_exempt
def example_core_page(request: HttpRequest):
    return HttpResponse("Hello world!")
