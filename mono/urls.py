from django.urls import path

from . import views
urlpatterns = [
  path('id',views.monoid_detail,name='detail')
]
