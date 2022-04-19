from django.http import HttpResponse
# from django.template import loader
from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = 'post_page.html'

    def get_context_data(self, **kwargs):
        # return super().get_context_data(**kwargs)
        return {'latest_question_list':[
        {'id': 2, 'question_text': 'first question'},
        {'id': 4, 'question_text': 'second question'},
        {'id': 3, 'question_text': 'third question'},
        {'id': 1, 'question_text': 'forth question'},
        {'id': 5, 'question_text': None},
    ]}


# def index_post(request):
#     latest_question_list = [
#         {'id': 2, 'question_text': 'first question'},
#         {'id': 4, 'question_text': 'second question'},
#         {'id': 3, 'question_text': 'third question'},
#         {'id': 1, 'question_text': 'forth question'},
#         {'id': 5, 'question_text': None},
#     ]

#     template = loader.get_template('post_page.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))
 

def post_page(requesr, number):
    if number == 1:
        return HttpResponse(
            'str 1 '
            'str 1 '

        )

    elif number ==2:
        return HttpResponse(
            'str 2 '
            'str 2 '

        )

    elif number ==3:
        return HttpResponse(
            'str 3 '
            'str 3 '

        )

    else: 
        return HttpResponse('another')