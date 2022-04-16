from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views.generic import View

# _______________
# from .models import Question

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
# _______________


class MyView(View):

    def get(self, request):
        if request.GET.get('type') == 'file':
            return FileResponse(open(static('img/image.jpg'), 'rb+'))
        elif request.GET.get('type') == 'json':
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == 'redirect':
            return HttpResponseRedirect('http://www.google.com')
        else:
            return HttpResponseNotAllowed("You shall not pass!!!")
        # print(request.GET)
        # return HttpResponse('this is get')

    def post(self, request):
        print(request.POST)
        return HttpResponse('this is post')


def main(request):
    # return HttpResponse('<button>Some Button</button>')
    return render(request, 'main.html')


def text(request):
    return HttpResponse('Text from backend to user interface')


def file(request):
    print(static('img/image.jpg/'))
    return FileResponse(open(static('img/image.jpg'), 'rb+'))


# def file(request):
#     print('lesson_3/static/img/image.jpg')
#     return FileResponse(open('lesson_3/static/img/image.jpg', 'rb+'))


def redirect(request):
    return HttpResponseRedirect('http://www.google.com')


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
