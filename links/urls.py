from django.urls import path
# from django.views.generic import TemplateView

from . import views

app_name = 'links'

urlpatterns = [
    # path("", views.indexLinks),
    path('', views.indexLinks, name='indexLinks'),
    path('painel/<int:link_id>/', views.painel_view, name='painel'),
]
   

