
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^patients/$', views.PatientList.as_view(), name='patient-list'),
    url(r'^patients-edit/(?P<pk>[0-9]+)/$', views.PatientEdit.as_view(), name='patient-edit'),

]