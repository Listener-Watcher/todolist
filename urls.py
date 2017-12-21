from django.conf.urls import url

from . import views

app_name = 'todolist'
urlpatterns = [
	url(r'^$', views.status_report, name='status_report'),#/todolist
	url(r'^$details/(?P<id>\w{0,50})/$',views.details),
	url(r'^add',views.add,name='add'),
	url(r'^delete',views.delete,name='delete'),
	url(r'^index',views.index,name='index'),
	url(r'^edit',views.edit,name='edit'),
	url(r'^changetime',views.changetime,name='changetime'),
	url(r'^marked',views.marked,name='marked'),
]