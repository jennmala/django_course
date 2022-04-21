from django.urls import path
from lesson_6 import views

urlpatterns = [
    path('try-form/', views.my_form, name='my_form'),
    path('class-form/', views.MyFormView.as_view(), name='class_form'),
    path('try-model-form/', views.ModelFormView.as_view(), name='model_form'),
]