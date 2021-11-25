from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

#path('list_of_employees/<str:department>/', views.Pay_slip_list , name='emp_pay_list'),

urlpatterns = [
	re_path(r'^admin/',admin.site.urls),
	re_path(r'^$', views.external,name='home'),
	re_path(r'^player', views.player,name='description'),
	re_path(r'^results', views.resultPage),
]

urlpatterns += staticfiles_urlpatterns()
