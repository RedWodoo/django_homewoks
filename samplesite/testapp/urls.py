from django.urls import path
from .views import SMSListView

urlpatterns = [
    path('sms/', SMSListView.as_view(), name='sms_list'),
]